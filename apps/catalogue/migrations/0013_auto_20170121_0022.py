# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-21 00:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0012_auto_20170121_0016'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='multipleoption',
            unique_together=set([]),
        ),
    ]