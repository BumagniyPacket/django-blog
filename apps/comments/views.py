from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, UpdateView

from apps.comments.forms import CommentForm
from apps.comments.models import Comment


class CommentApproveView(LoginRequiredMixin, UpdateView):
    model = Comment

    def get_success_url(self):
        self.object.approve()
        return self.object.article.get_absolute_url()


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        return self.object.article.get_absolute_url()


class CommentAddView(CreateView):
    form_class = CommentForm
    model = Comment
    http_method_names = ['post']

    def get_success_url(self):
        return self.object.article.get_absolute_url()

