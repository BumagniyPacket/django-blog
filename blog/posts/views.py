from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DeleteView, DetailView, ListView
from django.views.generic.edit import FormView, UpdateView

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
                Q(content__icontains=query) |
                Q(description__icontains=query)
            ).distinct()
        return qs


class PostDetail(DetailView):
    model = Post
    context_object_name = 'instance'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.object.draft and not self.request.user.is_superuser:
            raise Http404
        if not self.request.user.is_superuser:
            self.object.add_view()
            comments = self.object.comments.approved()
        else:
            comments = self.object.comments.all()
        context['comments'] = comments
        context['form'] = CommentForm()
        return context


class PostCreate(LoginRequiredMixin, FormView):
    form_class = PostForm
    template_name = 'posts/post_form.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user
        post.save()
        return redirect(post.get_absolute_url())


class PostUpdate(LoginRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'posts/post_form.html'

    def get_success_url(self):
        return self.object.get_absolute_url()


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
