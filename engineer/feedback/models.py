from django.db import models


# Create your models here.

class Feedback(models.Model):
    name = models.CharField('ФИО', max_length=50)
    job_title = models.CharField('Должность', max_length=50, null=True)
    text = models.TextField('Текст')
    time_create = models.DateTimeField("Дата создания", auto_now=True)

    def __str__(self):
        return f' {self.name} | {self.text} | {self.time_create}'

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
