# Generated by Django 3.0.8 on 2020-08-01 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
