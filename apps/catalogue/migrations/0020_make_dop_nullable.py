# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-06-29 18:20
from __future__ import unicode_literals

from django.db import migrations


def make_dop_nullable(apps, schema_editor):
    MultipleOption = apps.get_model("catalogue", "MultipleOption")

    MultipleOption.objects.filter(group__code="dop").update(is_required=False)


class Migration(migrations.Migration):
    dependencies = [
        ('catalogue', '0019_auto_20170623_2036'),
    ]

    operations = [
        migrations.RunPython(make_dop_nullable)
    ]
