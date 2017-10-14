from django.db import models

from blog.posts.models import Post


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    author = models.CharField(max_length=50, default='anon')
    timestamp = models.DateTimeField(auto_now=True)
    text = models.TextField(max_length=1000, default=None)
    approved = models.BooleanField(default=False)

    def approve(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.text
