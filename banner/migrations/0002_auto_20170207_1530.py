# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-07 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='position',
            field=models.IntegerField(choices=[(1, '\u0412 \u043b\u0435\u0432\u043e\u043c \u0431\u043b\u043e\u043a\u0435'), (2, '\u0412 \u0446\u0435\u043d\u0442\u0440\u0430\u043b\u044c\u043d\u043e\u043c \u0431\u043b\u043e\u043a\u0435')], verbose_name='\u041f\u043e\u0437\u0438\u0446\u0438\u044f'),
        ),
    ]
