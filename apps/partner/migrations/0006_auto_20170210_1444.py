# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-10 14:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0005_auto_20170210_1424'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockrecord',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='stockrecord',
            name='discount_type',
        ),
        migrations.RemoveField(
            model_name='stockrecord',
            name='discount_value',
        ),
    ]