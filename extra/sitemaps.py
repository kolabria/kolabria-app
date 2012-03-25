# -*- coding: utf-8 -*-

from pythontr_org.posts.models import Post, Category
from pythontr_org.links.models import Link
from pythontr_org.polls.models import Poll

from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from django.conf.urls.defaults import patterns


post_dict = {
    'queryset': Post.objects.published(),
    'date_field': 'created_at',
}


category_dict = {
    'queryset': Category.objects.all(),
}


links_dict = {
              'queryset': Link.objects.confirmed(),
              'date_field': 'created_at',
}


polls_dict = {
              'queryset': Poll.objects.all(),
              'date_field': 'created_at',
}


sitemaps = {
    'flatpages': FlatPageSitemap,
    
    'posts': GenericSitemap(post_dict, priority=0.5),
    'categories': GenericSitemap(category_dict, priority=1),
    'links': GenericSitemap(links_dict, priority=0.5),
    'polls': GenericSitemap(polls_dict, priority=0.5),
}


SITEMAPS_URLS = patterns('django.contrib.sitemaps.views',
    (r'^sitemap\.xml$', 'index', {'sitemaps': sitemaps}),
    (r'^sitemap-(?P<section>.+)\.xml$', 'sitemap', {'sitemaps': sitemaps}),
)