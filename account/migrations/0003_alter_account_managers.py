# Generated by Django 4.1.3 on 2022-12-10 13:03

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_account_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='account',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]