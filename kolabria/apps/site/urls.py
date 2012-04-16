from django.conf.urls import patterns, url


from kolabria.apps.site import views

urlpatterns = patterns('',
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^create/$', views.create_account, name='create'),
    url(r'^(?P<company>\w+)/admin/add/$', views.signup, name='admin'),
)
