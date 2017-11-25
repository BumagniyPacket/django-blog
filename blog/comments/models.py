from django.db import models
from django.urls import reverse

from blog.articles.models import Article


class CommentManager(models.Manager):
    def approved(self, article_id=None):
        if article_id:
            return super().filter(approved=True, article_id=article_id).order_by('-timestamp')
        return super().filter(approved=True).order_by('-timestamp')

    def all(self):
        return super().order_by('-timestamp')


class Comment(models.Model):
    class Meta:
        verbose_name = 'Блог - комментарий'
        verbose_name_plural = 'Блог - комментарии'

    objects = CommentManager()

    article = models.ForeignKey(Article, related_name='comments', verbose_name='Статья', on_delete=models.CASCADE)
    author = models.CharField(max_length=50, default='anon', verbose_name='Автор')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    text = models.TextField(max_length=1000, default=None, verbose_name='Текст комментария')
    approved = models.BooleanField(default=False, verbose_name='Подтвержден')

    def approve(self):
        self.approved = True
        self.save()

    def approve_link(self):
        return reverse('comments:approve', kwargs={'pk': self.pk})

    def delete_link(self):
        return reverse('comments:delete', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.author} - {self.text} | approved: {self.approved}'
