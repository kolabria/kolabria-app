from django.conf.urls import patterns, url
from kolabria.apps.account.models import AccountForm, UserProfileForm, UserForm

from kolabria.apps.site import views

urlpatterns = patterns('',
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^create/$', views.CreateAccount.as_view([AccountForm,
                                                   UserProfileForm, 
                                                   UserForm],
                                                  template_name='public/create-account.html')),
    url(r'^(?P<company>\w+)/admin/add/$', views.signup, name='admin'),
)
