# Generated by Django 3.1.3 on 2020-11-06 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_url',
            field=models.URLField(max_length=500),
        ),
    ]
