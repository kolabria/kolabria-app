# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User, Group

from django.contrib.sitemaps import ping_google
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe

#from kolabria.utils import slugify_unicode


GOOGLE_CODE_PRETTIFY = (u'''
    <a href='http://google-code-prettify.googlecode.com/svn/trunk/README.html' target='_blank'>
       Google Prettify
    </a>
''')


class Category(models.Model):
    """
    Category for Posts
    """
    name = models.CharField("Name", unique=True, max_length=50)
    slug = models.SlugField('Slug', max_length = 255, blank = True, null = True)
#    image = models.ImageField(upload_to='category_images')

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('posts:show_category', [self.slug]) 


    class Meta:
        verbose_name        = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']


def validate_user_is_in_authors_group(value):
    """
    Validate user is in the authors group
    """
    user  = User.objects.get(id = value)
    group = Group.objects.get(name = 'Yazarlar')

    if not user in group.user_set.all():
        raise ValidationError(u'%s is now authorized to write.' % user.username)


class PostManager(models.Manager):
    def published(self):
        return Post.objects.filter(published=True)


    def search(self, q):
        return Post.objects.published().filter(content__icontains=q)


class Post(models.Model):
    """
    Post model for posts
        'short_title': 35 character author title
        'short_content': 125 character short content
        'increase_read_count': Increment read count by one.
    """

    author = models.ForeignKey(
                               User,
                               verbose_name = "Author",
                               help_text = "Post Author",
                               validators = [validate_user_is_in_authors_group]
                               )

    title = models.CharField(
                             "title",
                             help_text = "Post title",
                             max_length=255
                            )
    category = models.ForeignKey(Category, verbose_name = "Category")
    slug = models.SlugField("Website URL")
    content = models.TextField(
                               "Contents of this post",
                               help_text = mark_safe('You HTML directly in this field. ' + GOOGLE_CODE_PRETTIFY),
                              )
    published = models.BooleanField(
                                    "Is Published",
                                    default=True,
                                    help_text = "Determines whether or not the post is published."
                                   )
    tags = models.CharField("Tags", max_length=100, help_text = "separate tags with commas (,)",
                            blank = True, null = True
                            )
    read_count = models.IntegerField("Read Count", default=0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects= PostManager()

    def __unicode__(self):
        return self.title


    @models.permalink
    def get_absolute_url(self):
        return ('posts:show', [self.category.slug, self.slug])


    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.slug = u"%s" % self.title

        super(Post, self).save(force_insert, force_update)

        try:
            ping_google()
        except Exception:
            pass

    def short_title(self):
        if len(self.title) > 34:
            return self.title[:35] + '...'
        else:
            return self.title

    def short_content(self):
        if len(self.content) > 124:
            return self.content[:125] + '...'
        else:
            return self.content 

    def increase_read_count(self):
        self.read_count += 1
        self.save()

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-created_at']
        get_latest_by = 'created_at'
