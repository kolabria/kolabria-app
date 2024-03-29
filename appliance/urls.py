from django.conf.urls.defaults import include, patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from appliance import views

urlpatterns = patterns('',
    url(r'^box/$', views.auth_box),
    url(r'^box/(?P<bid>\w+)/$', views.the_box),
    url(r'^box/unsubwall/(?P<bid>\w+)/$', views.unsubwall),
    url(r'^box/pubwall/(?P<bid>\w+)/$', views.pubwall),
    url(r'^appliances/$', views.appliances),
)
