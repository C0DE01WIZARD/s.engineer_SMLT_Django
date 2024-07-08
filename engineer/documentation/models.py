from django.db import models


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True, verbose_name="Описание")
    document = models.FileField(upload_to='documentation/documents/', verbose_name='Выберите файл')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Документы'
        verbose_name_plural = 'Документы'


class AddArticle(models.Model):
    name = models.CharField('Название', max_length=100)
    image = models.ImageField('Изображение', upload_to='article/', default='изображение любого формата')
    text = models.TextField('Текст', max_length=5000)
    type_article = models.CharField('Тип', max_length=50, default='')
    added = models.DateTimeField('Дата и время добавления', auto_now_add=True)
    url_article = models.SlugField('Слаг',max_length=150, unique=True, default='')
    is_published = models.BooleanField("Публикация", default=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.name
