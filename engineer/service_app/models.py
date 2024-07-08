from systems.models import *
from django.db import models


class Maintenance(models.Model):
    title = models.CharField('Название сервиса', max_length=50, default='')
    short_description = models.CharField('Короткое описание', max_length=255, default='')
    url = models.URLField('Ссылка', max_length=200, default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'

class Status(models.Model):
    status = models.CharField('Статус ТО', max_length=50)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Статус ТО'
        verbose_name_plural = 'Статусы ТО'



class Service(models.Model):
    address = models.ForeignKey(Address, verbose_name='Выберите адрес', on_delete=models.SET_NULL, null=True )
    location = models.ForeignKey(Location, verbose_name='Выберите локацию', on_delete=models.SET_NULL, null=True)
    equipments = models.ForeignKey(Equipment, verbose_name='Выберите оборудование', on_delete=models.SET_NULL, null=True)
    maintenance = models.ForeignKey(Maintenance, verbose_name='Выберите вид ТО', on_delete=models.SET_NULL, null=True)
    datetime = models.DateTimeField('Выберите дату проведения ТО')
    status = models.ForeignKey(Status, verbose_name='Выберите статус', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.maintenance

    class Meta:
        verbose_name = 'Назначение ТО'
        verbose_name_plural = 'Назначение ТО'
