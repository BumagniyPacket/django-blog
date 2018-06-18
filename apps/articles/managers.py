from django.db import models


class ArticleManager(models.Manager):
    def published(self):
        return super().filter(draft=False)
