# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-18 04:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comment', '0002_auto_20160311_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='c_Date',
            field=models.DateField(auto_now=True, verbose_name='评论日期'),
        ),
    ]
