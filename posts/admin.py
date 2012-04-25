# -*- coding: utf-8 -*-

from django.contrib import admin
from django import forms

from models import Post, Category


class CategoryAdmin(admin.ModelAdmin):
    search_fields       = ['name']
    prepopulated_fields = {'slug': ('name', )}


class PostAdmin(admin.ModelAdmin):
    fieldsets = (
      (u'Author and Category Details', {'fields': ('author', 'category')}),
      (u'Title and Content', {'fields': ('title', 'slug', 'content')}),
      (u'Published Data', {'fields': ('published', 'tags', 'read_count')})
    )

    save_on_top = True
    prepopulated_fields = {'slug': ('title', )}

    list_display  = ('title', 'category', 'author', 'published', 'read_count', 'created_at')    
    search_fields = ['title', 'content', 'tags']
    list_filter   = ('published', 'category', 'author')

    date_hierarchy = 'created_at'

    # admin actions
    actions = ['publish', 'unpublish']

    def publish(self, request, queryset):
        rows_updated = queryset.update(published = True)

        self.message_user(request, u"%s posts published successfully" % rows_updated)
    publish.short_description = u'Publish selected post'


    def unpublish(self, request, queryset):
        rows_updated = queryset.update(published = False)

        self.message_user(request, u"%s posts unpublished successfully!" % rows_updated)
    unpublish.short_description = u'Unpublish selected post'


    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'content':
            return db_field.formfield(widget=forms.Textarea(
                attrs={'cols': 100, 'rows': 30},
            ))
        return super(PostAdmin, self).formfield_for_dbfield(db_field, **kwargs)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
