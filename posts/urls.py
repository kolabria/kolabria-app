# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

from posts.views import PostListView, PostSearchListView,\
CategoryPostListView, MyPostListView, CategoryListView, NewPostView

urlpatterns = patterns('posts.views',
#     url(r'^$', PostListView.as_view(), name='index'),
    url(r'^posts/new/$', 'new', name='new'),
    url(r'^posts/new2/$', NewPostView.as_view(), name='new2'),

    url(r'^search/$', PostSearchListView.as_view(), name='search'),
    url(r'^categories/$', CategoryListView.as_view(), name='categories'),
    url(r'^my_posts/$', MyPostListView.as_view(), name='my_posts'),

    url(r'^(?P<slug>[^/]*)/$', CategoryPostListView.as_view(), name='show_category'),
    url(r'^(?P<category_slug>[^/]*)/(?P<slug>[^/]*)/$', 'show', name='show'),

    url(r'^posts/(?P<id>\d+)/edit/$', 'edit', name='edit'),
    url(r'^posts/(?P<id>\d+)/delete/$', 'delete', name='delete'),
)
