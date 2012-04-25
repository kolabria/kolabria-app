# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.formtools.wizard.views import SessionWizardView

from main.forms import ContactForm, AuthorForm
from main.mails import ContactMail, AuthorMail


def public(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/walls/')
    else:
        return HttpResponseRedirect('/')

def home(request):
    data = {'title': 'Kolabria - Real-time collaboration, made simple',}
    return render_to_response('main/home.html', data,
                              context_instance=RequestContext(request)) 

def create_account(request):
    data = {'title': 'Kolabria - Create a new company account and administrative user',}
    return render_to_response('main/create.html', data,
                              context_instance=RequestContext(request)) 


"""
def CreateAccount(SessionWizardView):
    def done(self, form_list, **kwargs):
        user_form = form_list[0]
        account_form = form_list[1]
        owner = user_form.save()
        account_form.instance.owner = owner
        new_account = account_form.save()
        return HttpResponseRedirect('/welcome/')
"""

def contact(request): 
    form = ContactForm(request.POST or None)
    
    if form.is_valid():
        
        ContactMail(form)
        return redirect('posts:index')                    
    
    return render(request, 'main/contact.html', locals())


@login_required
def became_an_author(request):    
    group         = Group.objects.get(name='Yazar olmak isteyenler')
    authors_group = Group.objects.get(name='Yazarlar')
    form          = AuthorForm(request.POST or None) 
    
    
    if group.user_set.filter(username=request.user):
        messages.success(request, u'Hali hazırda bir isteğiniz bulunmaktadır. Lütfen isteğinizin işlenmesini bekleyin.')
        
        return redirect('users:settings')
    
    
    if authors_group.user_set.filter(username=request.user):
        return redirect('users:settings')
    
    
    if request.method == 'POST':
        # Üyeyi 'Yazar olmak isteyenler' adlı gruba ekle
        
        if form.is_valid() and request.user.email:            
            group.user_set.add(request.user)        
            AuthorMail(request.user, form.cleaned_data)
            
            messages.success(request, u'İsteğiniz gönderilmiştir. Onaylandığında gönderi ekleyebileceksiniz. Size e-posta yoluyla geri döneceğiz.')        
            return redirect('users:settings')
        
    return render(request, 'main/became_an_author.html', locals())
