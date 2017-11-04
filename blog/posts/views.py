from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DeleteView, DetailView, ListView

from blog.comments.forms import CommentForm
from .forms import PostForm
from .models import Post


class PostsList(ListView):
    context_object_name = 'object_list'
    model = Post
    paginate_by = 10

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            qs = Post.objects.all()
        else:
            qs = Post.objects.published()

        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)
            ).distinct()
        return qs


class PostDetail(DetailView):
    model = Post
    context_object_name = 'instance'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)

        if not self.request.user.is_superuser:
            self.object.add_view()
            comments = self.object.comments.approved()
        else:
            comments = self.object.comments.all()
        context['comments'] = comments
        context['form'] = CommentForm()
        return context


def post_update(request, slug):
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


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/'


def add_comment(request, slug):
    instance = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = instance
            comment.save()
    return redirect(instance.get_absolute_url())
