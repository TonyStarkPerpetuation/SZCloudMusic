# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-19 02:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musician', '0002_auto_20191114_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='addtime',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='musician',
            name='like',
            field=models.IntegerField(verbose_name=b'\xe5\x96\x9c\xe6\xac\xa2'),
        ),
        migrations.AlterField(
            model_name='musician',
            name='music',
            field=models.FileField(upload_to=b'static/images', verbose_name=b'\xe9\x9f\xb3\xe4\xb9\x90\xe8\xb7\xaf\xe5\xbe\x84'),
        ),
        migrations.AlterField(
            model_name='musician',
            name='music_name',
            field=models.CharField(max_length=6, verbose_name=b'\xe6\xad\x8c\xe5\x90\x8d'),
        ),
        migrations.AlterField(
            model_name='musician',
            name='musician',
            field=models.CharField(max_length=10, verbose_name=b'\xe6\xad\x8c\xe6\x89\x8b'),
        ),
        migrations.AlterField(
            model_name='musician',
            name='picture',
            field=models.ImageField(upload_to=b'static/images', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe8\xb7\xaf\xe5\xbe\x84'),
        ),
        migrations.AlterField(
            model_name='musician',
            name='style',
            field=models.IntegerField(choices=[(1, b'\xe6\xb5\x81\xe8\xa1\x8c'), (2, b'\xe6\x91\x87\xe6\xbb\x9a'), (3, b'\xe7\x94\xb5\xe5\xad\x90'), (4, b'\xe6\xb0\x91\xe8\xb0\xa3'), (5, b'\xe7\x88\xb5\xe5\xa3\xab'), (6, b'\xe5\x85\xb6\xe4\xbb\x96')], default=1, verbose_name=b'\xe9\xa3\x8e\xe6\xa0\xbc'),
        ),
    ]
