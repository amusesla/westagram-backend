# Generated by Django 3.1 on 2020-09-03 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posting',
            old_name='user',
            new_name='writer',
        ),
    ]
