# Generated by Django 4.1.3 on 2022-12-23 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blogpost_date_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date_published',
            field=models.DateTimeField(auto_now=True, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='date_update',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date updated'),
        ),
    ]