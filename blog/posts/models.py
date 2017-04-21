from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils.safestring import mark_safe
from django.utils.text import slugify

# class PostManager(models.Manager):
#     def active(self, *args, **kwargs):
#         # Post.objects.all() = super(PostManager, self).all()
#         return super(PostManager, self).filter(draft=False)


# Create your models here.
from markdown import markdown


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=120)
    image = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"slug": self.slug})

    def get_delete_url(self):
        return '%sdelete' % self.get_absolute_url()

    def get_markdown(self):
        content = self.content
        markdown_text = markdown(content)
        return mark_safe(markdown_text)

    def add_view(self):
        self.views += 1
        self.save()

    def get_views(self):
        views = self.views
        return views

    class Meta:
        ordering = ['-timestamp', '-updated']


def create_slug(instance, new_slug=None):
    title = rus2eng(instance.title)
    slug = slugify(title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def rus2eng(text):
    """Converts a phone number with letters into its numeric equivalent."""
    char2number = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
        'е': 'e', 'ё': 'e', 'ж': 'j', 'з': 'z', 'и': 'i',
        'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
        'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
        'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch',
        'ш': 'sh', 'щ': 'shc', 'ъ': '', 'ы': 'i', 'ь': '',
        'э': 'e', 'ю': 'u', 'я': 'ya',
    }
    return ''.join(char2number.get(c, c) for c in text.lower())


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=Post)

if __name__ == '__main__':
    line = 'Привет как дела это слагифайный текст который я удалю после теста'
    new_line = rus2eng(line)
    print(new_line)
