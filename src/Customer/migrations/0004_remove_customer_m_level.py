# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-11 08:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0003_auto_20160311_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='m_Level',
        ),
    ]
