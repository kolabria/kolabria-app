# top-level views for the project, which don't belong in any specific app
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib import messages
from django.contrib.formtools.wizard.views import SessionWizardView
from django.views.generic.base import TemplateView

from kolabria.apps.account.models import AccountForm, UserProfileForm, UserForm

class HomePage(TemplateView):
    template_name = "public/home.html"


class CreateAccount(SessionWizardView):
    def done(self, form_list, **kwargs):
        # do something
        return HttpResponseRedirect('/welcome/')


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
