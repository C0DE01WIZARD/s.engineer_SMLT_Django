from django.db import models

# from purchase_app.models import *
from systems.models import *




# Create your models here.
class Status(models.Model):
    """Класс для создания статусов проишествия"""
    status_condition = models.CharField('Статус проишествия', max_length=10)

    def __str__(self):
        return self.status_condition

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статус'


class Types_incidents(models.Model):
    type = models.CharField("Тип проишествия", max_length=100)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Тип проишествия'
        verbose_name_plural = 'Тип проишествия'


class Danger_level(models.Model):
    type = models.CharField('Критичность', max_length=100)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Критичность'
        verbose_name_plural = 'Критичность'


class Incidents(models.Model):
    date = models.DateField('Дата проишествия')
    times = models.TimeField('Время проишествия')
    address = models.ForeignKey(Address, verbose_name='Выберите адрес', on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, verbose_name='Выберите оборудование', on_delete=models.CASCADE)
    danger_level = models.ForeignKey(Danger_level, verbose_name='Критичность', on_delete=models.CASCADE)
    types_incidents = models.ForeignKey(Types_incidents, verbose_name='Тип проишествия', on_delete=models.CASCADE)
    title = models.TextField('Описание проишествия', max_length=1000)
    incident_analysis = models.TextField('Анализ проишествия', max_length=100)
    status_condition = models.ForeignKey(Status, verbose_name='Выберите статус', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.date}/{self.address}/{self.types_incidents}/{self.title}'

    class Meta:
        verbose_name = 'Проишествие'
        verbose_name_plural = 'Проишествия'


class Forum(models.Model):
    topic_of_discussion = models.CharField("Тема обсуждения", max_length=100)
    name = models.CharField('ФИО', max_length=50)
    email_user = models.EmailField('Электронная почта', max_length=50)
    equipment = models.ForeignKey(Equipment, verbose_name='Выберите оборудование', on_delete=models.CASCADE)
    text_of_discussion = models.TextField('Введите текст для обсуждения')

    def __str__(self):
        return self.topic_of_discussion

    class Meta:
        verbose_name = 'Тема для обсуждения'
        verbose_name_plural = 'Темы для обсуждения'

class Defect(models.Model):
    location = models.ForeignKey(Location, verbose_name='Выберите локацию', on_delete=models.SET_NULL, null=True)
    address = models.ForeignKey(Address, verbose_name='Выберите адрес', on_delete=models.SET_NULL, null=True)
    system = models.ForeignKey(Systems, verbose_name='Выберите систему', on_delete=models.SET_NULL, null=True)
    equipment = models.ForeignKey(Equipment, verbose_name='Выберите оборудование', on_delete=models.SET_NULL, null=True)
    cause = models.CharField('Причина', max_length=100)
    # purchase = models.ForeignKey(Purchase, verbose_name='Выберите из списка закупку по данной несиправности',
    #                              on_delete=models.SET_NULL, null=True)
    elimination_period = models.IntegerField('Срок устранения, в днях')
    service_company = models.ForeignKey(Service_company, verbose_name='Компания, выполняющая работу',
                                        on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.location} / {self.address} / {self.system} / {self.cause}'

    class Meta:
        verbose_name = 'Неисправность'
        verbose_name_plural = 'Неисправности'
