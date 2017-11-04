from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, redirect, render

from blog.comments.forms import CommentForm

from .forms import PostForm
from .models import Post


def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, 'Successfully created')
        return redirect(instance.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, 'posts/post_form.html', context)


def post_detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    if not request.user.is_superuser:
        instance.add_view()
        comments = instance.comments.approved()
    else:
        comments = instance.comments.all()
    context = {
        'instance': instance,
        'form': CommentForm,
        'comments': comments
    }
    return render(request, 'posts/post_detail.html', context)


def post_list(request):
    if not request.user.is_staff or not request.user.is_superuser:
        queryset_list = Post.objects.published()
    else:
        queryset_list = Post.objects.all()

    # search
    query = request.GET.get('q')
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).distinct()

    # pagination
    paginator = Paginator(queryset_list, 5)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        'object_list': queryset,
        'title': 'List',
        'page_request_var': page_request_var
    }
    return render(request, 'posts/post_list.html', context)


def post_update(request, slug):
    print(slug)
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Successfully updated', extra_tags='html_safe')
        return redirect(instance.get_absolute_url())
    context = {
        'instance': instance,
        'form': form
    }
    return render(request, 'posts/post_form.html', context)


def post_delete(request, slug):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, 'Successfully deleted')
    return redirect('posts:list')


def add_comment(request, slug):
    instance = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = instance
            comment.save()
    return redirect(instance.get_absolute_url())
