# Generated by Django 3.1.3 on 2020-11-13 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0003_auto_20201109_2110'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posting',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='posting',
            old_name='updated',
            new_name='updated_at',
        ),
    ]
