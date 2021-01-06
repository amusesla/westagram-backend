# Generated by Django 2.2.5 on 2021-01-05 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=10, null=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('phone', models.CharField(max_length=45, null=True, unique=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
