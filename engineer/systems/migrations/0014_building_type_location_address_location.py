# Generated by Django 5.0.1 on 2024-02-10 13:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0013_alter_equipment_address_alter_equipment_system'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(max_length=55, verbose_name='Тип зданий')),
            ],
            options={
                'verbose_name': 'Тип',
                'verbose_name_plural': 'Тип',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, default='', max_length=55, verbose_name='Жилой комплекс, Социальный объект, Коммерческое здание')),
                ('year_of_construction_start', models.IntegerField(verbose_name='Год начала строительства')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='systems.building_type', verbose_name='Класс зданий')),
            ],
            options={
                'verbose_name': 'Объект',
                'verbose_name_plural': 'Объекты',
            },
        ),
        migrations.AddField(
            model_name='address',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='systems.location', verbose_name='Выберите локацию'),
        ),
    ]
