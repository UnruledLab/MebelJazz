# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-10-13 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0026_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='installation',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='\u0421\u0431\u043e\u0440\u043a\u0430, % \u043e\u0442 \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u0438'),
        ),
    ]
