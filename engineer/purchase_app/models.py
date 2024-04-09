from django.db import models

from incidents.models import Incidents
from systems.models import Systems, Address


# Create your models here.

class Status_purchase(models.Model):
    status_purchase = models.CharField('Статус закупки')

    def __str__(self):
        return self.status_purchase

    class Meta:
        verbose_name = 'Статус закупки'
        verbose_name_plural = 'Статус закупки'


class Select_necessuty(models.Model):
    select_necessuty = models.CharField('Необходимость закупки', max_length=50)

    def __str__(self):
        return self.select_necessuty

    class Meta:
        verbose_name = 'Необходимость закупки'
        verbose_name_plural = 'Необходимость закупок'




class Purchase(models.Model):
    """Создаем класс модели Закупки"""
    purchase = models.CharField('Наименование(материал, запчасть)', max_length=50)
    system = models.ForeignKey(Systems, on_delete=models.SET_NULL, verbose_name='Выберите систему', null=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, verbose_name='Адрес', null=True)
    price = models.CharField('Цена, в рублях', max_length=50)
    status = models.ForeignKey(Status_purchase, verbose_name='Статус закупки', on_delete=models.SET_NULL, null=True)
    necessity = models.ForeignKey(Select_necessuty, verbose_name='Необходимость', on_delete=models.SET_NULL, null=True)
    incident = models.ForeignKey(Incidents, verbose_name='Выберите проишествие в системе s.engineer', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.purchase

    class Meta:
        verbose_name = 'Закупка'
        verbose_name_plural = 'Закупки'
