from django.contrib import admin

from django import forms
from .models import *
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ArticleAdminForm(forms.ModelForm):
    text = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = AddArticle
        fields = '__all__'


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm

admin.site.register(Document)


@admin.register(AddArticle)
class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm

