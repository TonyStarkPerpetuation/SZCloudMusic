# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-19 02:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person_diary',
            name='content',
            field=models.CharField(max_length=500, verbose_name=b'\xe6\x97\xa5\xe8\xae\xb0\xe5\x86\x85\xe5\xae\xb9'),
        ),
        migrations.AlterField(
            model_name='person_diary',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, max_length=30, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='person_diary',
            name='diary_id',
            field=models.AutoField(auto_created=True, max_length=20, primary_key=True, serialize=False, verbose_name=b'\xe7\xbc\x96\xe5\x8f\xb7'),
        ),
        migrations.AlterField(
            model_name='person_photo',
            name='avatar',
            field=models.ImageField(default=b'', upload_to=b'avatar', verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f'),
        ),
        migrations.AlterField(
            model_name='person_photo',
            name='photo_id',
            field=models.AutoField(auto_created=True, max_length=20, primary_key=True, serialize=False, verbose_name=b'\xe7\x85\xa7\xe7\x89\x87\xe7\xbc\x96\xe5\x8f\xb7'),
        ),
    ]
