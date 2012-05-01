# top-level views for the project, which don't belong in any specific app
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib import messages

from django.contrib.formtools.wizard.views import SessionWizardView
from django.views.generic.base import TemplateView


class HomePage(TemplateView):
    template_name = "public/home.html"


class CreateAccount(SessionWizardView):
    def done(self, form_list, **kwargs):
        account_data = form_list[0]
        profile_data = form_list[1]
        user_data = form_list[2]

        owner = user_data.save()
        account_data.instance.owner = owner
        new_account = account_data.save()

        profile_data.instance.user = owner
        profile_data.instance.account = new_account
        profile = profile_data.save()
        
        return HttpResponseRedirect('http://%s.kolabria.com:8000' %
                                                          new_account.slug)


def signup(request, company):
    data = {'title': 'Kolabria Account: %s - Create an Account Owner user',
           }
    return render_to_response("public/signup.html", data,
                              context_instance=RequestContext(request))
