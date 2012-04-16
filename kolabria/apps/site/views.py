# top-level views for the project, which don't belong in any specific app
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib import messages

from django.views.generic.base import TemplateView

from kolabria.apps.account.models import AccountForm

class HomePage(TemplateView):
    template_name = "public/home.html"

def create_account(request):
    form = AccountForm(request.POST or None)
    if form.is_valid():
        # create the company account instance
        form.save()
        messages.success(request, form)
        return HttpResponseRedirect('/%s/signup' % form.slug )

    data = {'title': 'Kolabria - Create a new Account ', 'form': form,
             }
    return render_to_response("public/create.html", data,
                              context_instance=RequestContext(request))


def signup(request, company):
    data = {'title': 'Kolabria Account: %s - Create an Account Owner user',
           }
    return render_to_response("public/signup.html", data,
                              context_instance=RequestContext(request))
"""
# also attach the contact information to the anonymous request.user
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password2']
        new_user = User.create_user(username=username, email=email,
                                    password=password)
        new_user.first_name = request.POST['first_name']
        new_user.last_name = request.POST['last_name']
        new_user.save()
        auth_user = authenticate(username=username, password=password)
        login(request=request, user=auth_user)
        messages.success(request, 'Successfully logged in as %s' % \
                                                           auth_user.username)
"""
