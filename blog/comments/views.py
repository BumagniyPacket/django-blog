from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView, UpdateView

from blog.comments.models import Comment


class CommentApproveView(LoginRequiredMixin, UpdateView):
    model = Comment

    def get_success_url(self):
        self.object.approve()
        return self.object.post.get_absolute_url()


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        return self.object.post.get_absolute_url()
