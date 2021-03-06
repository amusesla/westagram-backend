# Generated by Django 3.1.3 on 2020-12-04 09:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0003_auto_20201203_0721'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.CharField(max_length=1000)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 12, 4, 18, 57, 20, 93179))),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'posts',
            },
        ),
    ]
