# Generated by Django 3.0.8 on 2020-08-05 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_auto_20200803_2127'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='users',
        ),
    ]