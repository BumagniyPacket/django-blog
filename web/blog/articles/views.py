from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import Http404
from django.shortcuts import redirect
from django.views.generic import DeleteView, DetailView, ListView
from django.views.generic.edit import FormView, UpdateView

from blog.utils.mixins import CacheMixin
from .forms import ArticleForm
from .models import Article


class ArticlesListView(CacheMixin, ListView):
    context_object_name = 'object_list'
    model = Article
    paginate_by = 10

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            qs = Article.objects.all()
        else:
            qs = Article.objects.published()

        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(description__icontains=query)
            ).distinct()
        return qs


class ArticleDetailView(CacheMixin, DetailView):
    model = Article
    context_object_name = 'instance'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.object.draft and not self.request.user.is_superuser:
            raise Http404
        if not self.request.user.is_superuser:
            self.object.add_view()

        return context


class ArticleCreateView(LoginRequiredMixin, FormView):
    form_class = ArticleForm
    template_name = 'articles/article_form.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user
        post.save()
        return redirect(post.get_absolute_url())


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ArticleForm
    model = Article
    template_name = 'articles/article_form.html'

    def get_success_url(self):
        return self.object.get_absolute_url()


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    success_url = '/'
