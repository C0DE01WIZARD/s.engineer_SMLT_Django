# Generated by Django 5.0.2 on 2024-04-25 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentation', '0012_alter_addarticle_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addarticle',
            name='url',
        ),
        migrations.AddField(
            model_name='addarticle',
            name='url_article',
            field=models.SlugField(blank=True, default='', editable=False, max_length=150, null=True),
        ),
    ]
