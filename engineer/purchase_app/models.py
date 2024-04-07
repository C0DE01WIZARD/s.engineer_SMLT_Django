from django.db import models

# Create your models here.

class Purchase(models.Model):
    """Создаем класс модели Оборудование"""
    purchase = models.CharField('Наименование', max_length=50)
    system = models.ForeignKey(Systems, on_delete=models.PROTECT,verbose_name='Выберите систему')
    address = models.ForeignKey(Address, on_delete=models.PROTECT, verbose_name='Адрес', default='')
    price = models.CharField('Цена, в рублях', max_length=50)
    necessity = models.ForeignKey(Location, verbose_name='Локация', on_delete=models.PROTECT, default='')
    status = models.ForeignKey(Company, verbose_name='Юридическое лицо', on_delete=models.PROTECT, default='' )



    def __str__(self):
        return self.purchase

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудования'