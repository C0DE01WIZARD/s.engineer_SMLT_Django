# Generated by Django 5.0.2 on 2024-04-09 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0009_equipment_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='passport_number',
            field=models.IntegerField(blank=True, default='', null=True, verbose_name='Номер в паспорте (при наличии)'),
        ),
    ]