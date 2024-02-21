from django.db import models


class Employees(models.Model):
    full_name = models.CharField('ФИО сотрудника', max_length=100)
    job_title = models.CharField('Должность', max_length=50)
    in_company = models.DateTimeField('Дата приема на работу')

