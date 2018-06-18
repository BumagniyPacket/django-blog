from django.views.decorators.cache import cache_page
from django.conf import settings

from apps.common.utils import create_slug


CACHE_TTL = getattr(settings, 'CACHE_TTL', 360)


class CacheMixin:  # pragma: no cover
    """Кэшируем страницы"""
    cache_timeout = CACHE_TTL

    def get_cache_timeout(self):
        return self.cache_timeout

    def dispatch(self, *args, **kwargs):
        return cache_page(
            self.get_cache_timeout())(
            super(CacheMixin, self).dispatch)(*args, **kwargs)


class GenerateSlugMixin:
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = create_slug(self)
        super().save(*args, **kwargs)
