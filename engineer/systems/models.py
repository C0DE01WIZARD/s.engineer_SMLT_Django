from django.db import models


class Building_type(models.Model):
    types = models.CharField('Тип зданий', max_length=55)

    def __str__(self):
        return f'{self.types}'

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Тип'


class Location(models.Model):
    location = models.CharField('Жилой комплекс, Социальный объект, Коммерческое здание', max_length=55)
    year_of_construction_start = models.IntegerField('Год начала строительства')
    category = models.ForeignKey(Building_type, on_delete=models.CASCADE,
                                 verbose_name='Класс зданий')

    def __str__(self):
        return f'{self.location}'

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'


class Company(models.Model):
    name = models.CharField('Название юридического лица', max_length=255)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Address(models.Model):
    location = models.ForeignKey(Location, verbose_name='Выберите локацию', on_delete=models.CASCADE)
    city = models.CharField('Город', max_length=50)
    settlement = models.CharField('Поселение', max_length=50)
    street = models.CharField('Улица', max_length=50)
    home = models.CharField('Дом', max_length=50)

    def __str__(self):
        return f'г.{self.city}, поселение {self.settlement}, улица {self.street}, дом {self.home}'

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


class Quality_of_service(models.Model):
    quality = models.CharField('Качество обслуживания', max_length=10)

    def __str__(self):
        return f'{self.quality}'

    class Meta:
        verbose_name = 'Качество обслуживания'
        verbose_name_plural = 'Качество обслуживания'


class Service_company(models.Model):
    names_company = models.CharField('Название компании', max_length=50)
    contract_number = models.CharField('Номер договора', max_length=50)
    image = models.ImageField('Изображение', upload_to='service_company/', default='изображение любого формата',
                              null=True)
    title = models.TextField('Деятельность компании', max_length=500, default='')
    company_director = models.CharField('ФИО директора компании', max_length=100)
    quality_of_service = models.ForeignKey(Quality_of_service, on_delete=models.CASCADE,
                                           verbose_name='Качество обслуживания от 1 до 5')
    phone = models.CharField("Номер телефона аварийной бригады", max_length=12, default='')

    def __str__(self):
        return self.names_company

    class Meta:
        verbose_name = 'Сервисная компания'
        verbose_name_plural = 'Сервисные компании'


class Systems(models.Model):
    system_name = models.CharField('Наименование системы', max_length=50)
    title = models.TextField('Описание', max_length=500)
    full_name = models.CharField("Полное название", max_length=100)
    image = models.ImageField('Изображение', upload_to='systems/', default='изображение любого формата',
                              null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name='Локация', default='')
    service_company = models.ForeignKey(Service_company, on_delete=models.CASCADE,
                                        verbose_name='Сервисная компания по обслуживанию')
    url = models.URLField('Ссылка', default='')
    cat_id = models.IntegerField('Категория', default='1')

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
    passport_number = models.IntegerField('Номер в паспорте (при наличии)', null=True, blank=True, default='')
    quantity = models.IntegerField('Количество', null=True, blank=True)
    location = models.ForeignKey(Location, verbose_name='Локация', on_delete=models.PROTECT, default='')
    company = models.ForeignKey(Company, verbose_name='Юридическое лицо', on_delete=models.PROTECT, default='')
    address = models.ForeignKey(Address, on_delete=models.PROTECT, verbose_name='Адрес', default='')
    cat_id = models.IntegerField('Категория', default='1')

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
