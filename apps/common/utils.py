from django.db.models import Q
from django.utils.text import slugify


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title, allow_unicode=True)
    if new_slug is not None:
        slug = new_slug
    qs = instance.__class__.objects.filter(
        Q(slug=slug) | Q(slug__startswith=slug)
    )
    if qs.exists():
        slug = '%s-%s' % (slug, qs.count())
    return slug
