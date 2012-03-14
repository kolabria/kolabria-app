# -*- coding: utf-8 -*-

from django.forms import ModelForm

from pythontr_org.posts.models import Post, Category


class PostForm(ModelForm):
    
    
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'input-xlarge'
    
    
    class Meta:
        model = Post
        
        exclude = ('created_at', 'updated_at', 'read_count', 'author', 'slug')