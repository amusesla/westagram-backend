# Generated by Django 3.1.1 on 2020-10-11 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20201011_0544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
    ]