from django.db import models
from django.urls import reverse

from blog.posts.models import Post


class CommentManager(models.Manager):
    def approved(self):
        return super().filter(approved=True).order_by('-timestamp')

    def all(self):
        return super().order_by('-timestamp')


class Comment(models.Model):
    class Meta:
        verbose_name = 'Блог - комментарий'
        verbose_name_plural = 'Блог - комментарии'

    objects = CommentManager()

    post = models.ForeignKey(Post, related_name='comments')
    author = models.CharField(max_length=50, default='anon')
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=1000, default=None)
    approved = models.BooleanField(default=False)

    def approve(self):
        self.approved = True
        self.save()

    def approve_link(self):
        return reverse('comments:approve', kwargs={'pk': self.pk})

    def delete_link(self):
        return reverse('comments:delete', kwargs={'pk': self.pk})

    def __str__(self):
        return self.text
