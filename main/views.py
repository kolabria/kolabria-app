#u -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.formtools.wizard.views import SessionWizardView

from main.forms import CreateAccountForm, SignUpForm
from main.forms import TestForm, ContactForm, AuthorForm 
from main.mails import ContactMail, AuthorMail
from users.forms import UserEmailCreationForm
from users.models import Account, AccountForm, Profile, ProfileForm
from django.contrib.auth.models import User

import ipdb

def signup(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        new_user = form.save()
        new_user = authenticate(username=request.POST['username'], 
                                password=request.POST['password1'])
        user = authenticate(user=new_user, password=request.POST['password1'])
        login(request, new_user)
        return HttpResponseRedirect('/accounts/create/')

    data = {'title': 'Kolabria - Create an Account', 'form': form,}
    return render_to_response('main/simple.html', data, 
                              context_instance=RequestContext(request))


def testsimple(request):
    form = TestForm(request.POST or None) 
    if form.is_valid():
        ipdb.set_trace()
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password1']
        new_user = User.objects.create_user(username=username,
                                        email=email,
                                        password=password)
        new_user.save()
        user = authenticate(user=new_user, password=password)
        login(request, user) 
        company = form.cleaned_data['company']
        subdomain = form.cleaned_data['subdomain']
        account = Account.objects.create(company=company,
                                         subdomain=subdomain,
                                         owner=user)
        account.save()
        profile = user.profile.account=account
        profile.save()
        messages.success(request, u'Successfully created new account and owner')
        return HttpResponseRedirect('http://%s.kolabria.com:8000/welcome/' % \
                                                          form.cleaned_data['subdomain'])
    data = {'title': 'Kolabria - Create an Account and account owner',
            'form': form,}
    return render(request, 'main/simple.html', locals())

def testcreate(request):
    form = TestForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username'] 
            email = form.cleaned_data['email']

    #        company = form.instance.company
    #        form.save()
            msg = 'Successfully processed form: %s' % form.data
            messages.success(request, msg)
            messages.success(request, request.subdomain)
            sub_url = '%s.kolabria.com:8000/welcome/' % \
                                                         form.cleaned_data['subdomain']
            return HttpResponseRedirect(sub_url)
#           return redirect('main:welcome')

    data = {'title': 'Kolabria - Simple Signup', 'form': form,}
    return render_to_response('main/create.html', data,
                              context_instance=RequestContext(request))

@login_required
def welcome(request):
    subdomain = request.subdomain
    profile = request.user.profile
    data = {'title': 'Kolabria - Welcome Account Owner',
            'profile': profile,
            'subdomain': subdomain, }
    return render_to_response('main/welcome.html', data,
                              context_instance=RequestContext(request)) 


def public(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/walls/')
    else:
        return HttpResponseRedirect('/')

def home(request):
    data = {'title': 'Kolabria - Real-time collaboration, made simple',}
    return render_to_response('main/home.html', data,
                              context_instance=RequestContext(request)) 

def create(request):
    account_form = AccountForm(request.POST or None)
    user_form = UserEmailCreationForm(request.POST or None)
    if account_form.is_valid() and user_form.is_valid():
        messages.success(request, 'AccountForm and UserEmailCreatioForm are valid')
        return HttpResponseRedirect('/welcome/')

    data = {'title': 'Kolabria - Create Account', 'form': account_form,
            'user_form': user_form, }

    return render_to_response('main/create.html', data,
                              context_instance=RequestContext(request))

def create_account(request):
    form = AccountForm(request.POST or None)
    if form.is_valid():
        form.instance.owner = request.user
        account = form.save()

        # Create profile for account owner, link to Account
        profile = Profile.objects.create(user=request.user, account=account)
        profile.admin = profile.account.owner
        profile.save()

        msg = 'Successfully created Account: %s with Owner: %s'
        messages.success(request, msg % (account.company, request.user.username))
        return HttpResponseRedirect('http://%s.kolabria.com:8000/accounts/welcome/' % \
                                                                      account.subdomain)

    data = {'title': 'Kolabria - Create a new company account and administrative user',
            'form': form,}

    return render_to_response('main/create.html', data,
                              context_instance=RequestContext(request)) 


def CreateAccount(SessionWizardView):
    def done(self, form_list, **kwargs):
        user_form = form_list[0]
        account_form = form_list[1]
        owner = user_form.save()
        account_form.instance.owner = owner
        new_account = account_form.save()
        return HttpResponseRedirect('/welcome/')


def contact(request): 
    form = ContactForm(request.POST or None)
    
    if form.is_valid():
        
        ContactMail(form)
        return redirect('posts:index')                    
    
    return render(request, 'main/contact.html', locals())


@login_required
def became_an_author(request):    
    group = Group.objects.get(name='Yazar olmak isteyenler')
    authors_group = Group.objects.get(name='Yazarlar')
    form = AuthorForm(request.POST or None) 

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
