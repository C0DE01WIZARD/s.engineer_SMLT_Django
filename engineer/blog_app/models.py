from django.db import models


class Blog(models.Model):
    blog = models.CharField('Блог', max_length=50)
    title = models.CharField('Описание', max_length=200)

    def __str__(self):
        return self.blog

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блог'
