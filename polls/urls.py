# -*- coding: utf-8-*-

from django.conf.urls.defaults import url, patterns

from kolabria.polls.views import PollListView, PollDetailView

urlpatterns = patterns('kolabria.polls.views',
    url(r'^$', PollListView.as_view(), name='index'),
    url(r'^(?P<slug>[^/]*)/$', PollDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[^/]*)/results/$', PollDetailView.as_view(template_name='polls/results.html'), name='results'),
    url(r'^(?P<slug>[^/]*)/vote/$', 'vote', name='vote'),
    url(r'^(?P<slug>[^/]*)/vote/back/', 'vote_back', name='vote_back'),
)
