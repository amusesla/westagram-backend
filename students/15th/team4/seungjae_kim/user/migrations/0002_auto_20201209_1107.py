# Generated by Django 3.1.4 on 2020-12-09 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=256, verbose_name='사용자 비밀번호'),
        ),
    ]