# Generated by Django 4.2.6 on 2023-10-25 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidents',
            name='incident_analysis',
            field=models.TextField(max_length=100, verbose_name='Анализ проишествия'),
        ),
    ]