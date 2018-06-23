from django.db import models


class Tag(models.Model):
    class Meta:
        verbose_name = 'Блог - тег'
        verbose_name_plural = 'Блог - теги'

    name = models.CharField(verbose_name='Имя', max_length=35, unique=True)

    def __str__(self):
        return self.name
