from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = 'Блог - категория'
        verbose_name_plural = 'Блог - категории'

    name = models.CharField(verbose_name='Имя', max_length=35, unique=True)
    description = models.TextField(verbose_name='Описание', max_length=200)

    def __str__(self):
        return self.name

