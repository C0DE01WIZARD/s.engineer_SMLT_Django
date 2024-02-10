from django.db import models


# Create your models here.
class Building_type(models.Model):
    types = models.CharField('Тип зданий', max_length=55)

    def __str__(self):
        return f'{self.types}'

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Тип'


class Location(models.Model):
    location = models.CharField('Жилой комплекс, Социальный объект, Коммерческое здание', max_length=55, blank=True,
                                default='')
    year_of_construction_start = models.IntegerField('Год начала строительства')
    category = models.ForeignKey(Building_type, on_delete=models.CASCADE,
                                 verbose_name='Класс зданий')

    def __str__(self):
        return f'{self.location}'

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'


class Address(models.Model):
    location = models.ForeignKey(Location, verbose_name='Выберите локацию', on_delete=models.CASCADE, null=True)
    city = models.CharField('Город', max_length=50, blank=True, default='')
    settlement = models.CharField('Поселение', max_length=50, blank=True, default='')
    street = models.CharField('Улица', max_length=50, blank=True, default='')
    home = models.CharField('Дом', max_length=50, blank=True, default='')
    corps = models.CharField('Корпус', max_length=50, blank=True, default='')

    def __str__(self):
        return f'г.{self.city}, поселение {self.settlement}, улица {self.street}, дом {self.home}{self.corps}'

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


class Quality_of_service(models.Model):
    quality = models.CharField('Качество обслуживания')

    def __str__(self):
        return f'{self.quality}'

    class Meta:
        verbose_name = 'Качество обслуживания'
        verbose_name_plural = 'Качество обслуживания'


class Service_company(models.Model):
    names_company = models.CharField('Название компании', max_length=50)
    contract_number = models.CharField('Номер договора', max_length=50)
    company_director = models.CharField('ФИО директора компании', max_length=100)
    quality_of_service = models.ForeignKey(Quality_of_service, on_delete=models.CASCADE,
                                           verbose_name='Качество обслуживания от 1 до 5')

    # phone = models.CharField("Номер телефона аварийной бригады", max_length=12)

    def __str__(self):
        return self.names_company

    class Meta:
        verbose_name = 'Сервисная компания'
        verbose_name_plural = 'Сервисные компании'


class Systems(models.Model):
    system_name = models.CharField('Наименование системы', max_length=50)
    title = models.TextField('Описание', max_length=500, default='')
    full_name = models.CharField("Полное название", max_length=100, default='')
    location = models.CharField('Местонахождение', max_length=50)
    service_company = models.ForeignKey(Service_company, on_delete=models.CASCADE,
                                        verbose_name='Сервисная компания по обслуживанию')

    def __str__(self):
        return self.system_name

    class Meta:
        verbose_name = 'Система'
        verbose_name_plural = 'Системы'


class Equipment(models.Model):
    """Создаем класс модели Оборудование"""
    equipment = models.CharField('Название оборудования', max_length=50)
    system = models.ForeignKey(Systems, on_delete=models.PROTECT,
                               verbose_name='Выберите систему')
    manufacturer = models.CharField('Производитель', max_length=50)
    model = models.CharField('Модель оборудования', max_length=50)
    year = models.IntegerField('Год ввода в эксплуатацию')
    address = models.ForeignKey(Address, on_delete=models.PROTECT, verbose_name='Адрес', default='')

    number = models.CharField("Номер ИТП (если присвоено)", max_length=20, default='')

    def __str__(self):
        return self.equipment

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудования'


class Tasks(models.Model):
    tasks = models.CharField("Задача", max_length=255)
    datetime = models.DateTimeField("Выполнить до")

    def __str__(self):
        return self.tasks

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
