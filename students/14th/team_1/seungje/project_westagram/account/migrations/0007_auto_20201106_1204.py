# Generated by Django 3.1.3 on 2020-11-06 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20201106_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='user_password',
            field=models.CharField(default='', max_length=40),
        ),
    ]
