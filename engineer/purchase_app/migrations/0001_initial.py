# Generated by Django 5.0.2 on 2024-04-09 17:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('systems', '0010_alter_equipment_passport_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Select_necessuty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select_necessuty', models.CharField(max_length=50, verbose_name='Необходимость закупки')),
            ],
            options={
                'verbose_name': 'Необходимость закупки',
                'verbose_name_plural': 'Необходимость закупок',
            },
        ),
        migrations.CreateModel(
            name='Status_purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_purchase', models.CharField(verbose_name='Статус закупки')),
            ],
            options={
                'verbose_name': 'Закупка',
                'verbose_name_plural': 'Закупки',
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase', models.CharField(max_length=50, verbose_name='Наименование(материал, запчасть)')),
                ('price', models.CharField(max_length=50, verbose_name='Цена, в рублях')),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='systems.address', verbose_name='Адрес')),
                ('system', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='systems.systems', verbose_name='Выберите систему')),
                ('necessity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='purchase_app.select_necessuty', verbose_name='Необходимость')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='purchase_app.status_purchase', verbose_name='Статус закупки')),
            ],
            options={
                'verbose_name': 'Оборудование',
                'verbose_name_plural': 'Оборудования',
            },
        ),
    ]