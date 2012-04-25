# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required

from django.contrib import messages
from django.views.generic import ListView, CreateView

from posts.models import Post, Category
from posts.forms import PostForm

from utils import ProtectedView


class PostListView(ListView):
    queryset=Post.objects.published()
    paginate_by=20

    template_name='posts/index.html'
    template_object_name='post'


class PostSearchListView(PostListView):
    template_name='posts/search.html'

    def get_queryset(self):
        return Post.objects.search(self.request.GET.get('q', ''))


    def get_context_data(self, **kwargs):
        context = super(PostSearchListView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')

        return context


class CategoryPostListView(PostListView):
    template_name='posts/category_show.html'

    def get_queryset(self):
        self.category=get_object_or_404(Category, slug=self.kwargs['slug'])
        return self.category.post_set.filter(published=True)


    def get_context_data(self, **kwargs):
        context = super(CategoryPostListView, self).get_context_data(**kwargs)
        context['category'] = self.category

        return context


class CategoryListView(ListView):
    model = Category
    paginate_by = 16
    template_name = 'posts/categories.html'
    template_object_name = 'category_list'


class MyPostListView(PostListView, ProtectedView):
    template_name = 'posts/my_posts.html'
    paginate_by = 6

    def get_queryset(self):
        return self.request.user.post_set.all()


def show(request, category_slug, slug):
    """
        Show post or 404 if not found
    """

    post = get_object_or_404(Post, slug = slug, published = True, category__slug = category_slug)
    post.increase_read_count()

    return render(request, 'posts/show.html', locals())


# Add new post, edit, delete

@permission_required('posts.add_post')
def new(request):
    """
    Used to add new posts
    """

    post = Post(author = request.user)
    form = PostForm(request.POST or None, instance = post)

    if form.is_valid():
        form.save()
        messages.success(request, u'Post deleted successfully')
        return redirect('posts:my_posts')

    return render(request, 'posts/new.html', locals())


class NewPostView(CreateView):
    template_name = 'posts/new.html'
    #form_class = PostForm

    def get_form_class(self):
        post = Post(author = self.request.user)

        return PostForm(instance=post)


@permission_required('posts.change_post')
def edit(request, id):
    """
    Edit details of post
    """

    post = get_object_or_404(Post, id=id)

    # If request.user is not the owner of the post
    # redirect to access denied page

    if not post.author == request.user:
        return redirect('access_denied')

    form = PostForm(request.POST or None, instance = post)

    if form.is_valid():
        form.save()
        messages.success(request, u'Post edited successfully')
        return redirect('posts:my_posts')

    return render(request, 'posts/edit.html', locals())


@permission_required('posts.delete_post')
def delete(request, id):
    """
    Post deleted successfully
    """
    post = get_object_or_404(Post, id = id)
    if not request.user == post.author:
        return redirect('access_denied')
    post.delete()
    messages.success(request, u'"%s" was successfully deleted' % post.title)
    return redirect('posts:my_posts')
