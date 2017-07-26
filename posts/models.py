from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from markdown import markdown


class PostManager(models.Manager):
    def published(self, *args, **kwargs):
        return super(PostManager, self).filter(draft=False)


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=120)
    image = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)

    objects = PostManager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = create_slug(self)
        super(Post, self).save(*args, **kwargs)

    def get_comments(self):
        return self.comments.all().order_by('-timestamp')

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"slug": self.slug})

    def get_delete_url(self):
        return '%sdelete' % self.get_absolute_url()

    def get_edit_url(self):
        return '%sedit' % self.get_absolute_url()

    def add_view(self):
        self.views += 1
        self.save()

    def get_views(self):
        views = self.views
        return views

    class Meta:
        ordering = ['-timestamp', '-updated']


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title, allow_unicode=True)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug
