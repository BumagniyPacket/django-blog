from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify


class ArticleManager(models.Manager):
    def published(self):
        return super().filter(draft=False)


class Article(models.Model):
    class Meta:
        verbose_name = 'Блог - пост'
        verbose_name_plural = 'Блог - посты'

        ordering = ['-timestamp', '-updated']

    objects = ArticleManager()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, verbose_name='Пользователь')
    title = models.CharField(max_length=120, verbose_name='Заголовок поста')
    image = models.URLField(blank=True, verbose_name='Ссылка на изображение')
    description = models.TextField(max_length=400, verbose_name='Описание поста')
    slug = models.SlugField(unique=True, blank=True, verbose_name='Слаг')
    content = models.TextField(verbose_name='Контент')
    draft = models.BooleanField(default=False, verbose_name='В процессе написания')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    views = models.IntegerField(default=0, verbose_name='Просмотров')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = create_slug(self)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('articles:delete', kwargs={'slug': self.slug})

    def get_edit_url(self):
        return reverse('articles:edit', kwargs={'slug': self.slug})

    def add_view(self):
        self.views += 1
        self.save()

    def get_views(self):
        views = self.views
        return views


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title, allow_unicode=True)
    if new_slug is not None:
        slug = new_slug
    qs = Article.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = '%s-%s' % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug
