# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required

from django.contrib import messages

from pythontr_org.posts.models import Post, Category
from pythontr_org.posts.forms import PostForm

from pythontr_org.posts.utils import posts_object_list


def index(request):
    """
        Gönderileri listelemek için kullanılır.
    """    
    return posts_object_list(
                       request,
                       queryset=Post.objects.filter(published = True),
                       template_name='index.html',
                       )


def show(request, category_slug, slug):
    """
        Gönderiyi göstermek için kullanılır.
        Eğer gönderi bulunamazsa 404 döndürür.
    """
    
    post = get_object_or_404(Post, slug = slug, published = True)
    post.increase_read_count()
    
    return render(request, 'posts/show.html', locals())


def search(request):
    """
        Gönderileri aramak için kullanılır.
        Aranan yapı Post modelinin 'content' alında bulunuyorsa seçer.
    """
    
    q = request.GET.get('q', '')
    return posts_object_list(request,
                       queryset=Post.objects.filter(content__icontains = q), 
                       template_name='search.html',
                       extra_context=locals(),
                       )

# Kategoriler ile ilgili.

def category_show(request, slug):
    """
        Bu kategoriye bağlı gönderileri bulmak için kullanılır.
        Eğer kategori bulunmazsa 404 döndürür.
    """
    
    category = get_object_or_404(Category, slug = slug)    
    return posts_object_list(request,
                       queryset=category.post_set.all(),
                       template_name='category_show.html',
                       extra_context=locals(),
                       )


# yeni gönderi ekleme, düzenleme ve silme

@permission_required('posts.add_post')
def new(request):
    """
        Yeni gönderi eklemek için kullanılır.
    """
    
    
    post = Post(author = request.user)
    
    form = PostForm(request.POST or None, instance = post)
    
    if form.is_valid():
        form.save()
        
        messages.success(request, u'Gönderi başarı ile eklendi.')
        return redirect('posts:my_posts')    
        

    return render(request, 'posts/new.html', locals())


@permission_required('posts.change_post')
def edit(request, id):
    """
        Gönderiyi düzenlemek için kullanılır.
    """
    
    post = get_object_or_404(Post, id = id)
    
    # eğer request.user gönderinin sahibi değilse
    # erişim engellendi sayfasına yönlendir.
    
    if not post.author == request.user:
        return redirect('access_denied')
    
    form = PostForm(request.POST or None, instance = post)
    
    if form.is_valid():
        form.save()
        
        messages.success(request, u'Gönderi başarı ile düzenlendi.')
        
        return redirect('posts:my_posts')
    
        
    return render(request, 'posts/edit.html', locals())


@permission_required('posts.add_post')
def my_posts(request):
    """
        Yazarın kendi gönderdiği gönderilerin listelendiği
        düzenle ve sil bağlantılarının yer aldığı sayfa.
    """
    
    posts = request.user.post_set.all()
    
    return render(request, 'posts/my_posts.html', locals())
    
    
@permission_required('posts.delete_post')
def delete(request, id):
    """
        Gönderi silmek için kullanılır.
    """
    
    post = get_object_or_404(Post, id = id)
    
    if not request.user == post.author:
        return redirect('access_denied')
    
    post.delete()
    
    messages.success(request, u'"%s" başlıklı gönderi başarı ile silindi' % post.title)
    
    return redirect('posts:my_posts')
    