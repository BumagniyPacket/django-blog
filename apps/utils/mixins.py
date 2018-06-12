from django.views.decorators.cache import cache_page
from django.conf import settings

CACHE_TTL = getattr(settings, 'CACHE_TTL', 360)


class CacheMixin:
    """Кэшируем страницы"""
    cache_timeout = CACHE_TTL

    def get_cache_timeout(self):
        return self.cache_timeout

    def dispatch(self, *args, **kwargs):
        return cache_page(
            self.get_cache_timeout())(
            super(CacheMixin, self).dispatch)(*args, **kwargs)

