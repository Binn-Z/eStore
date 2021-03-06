# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-11 08:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0002_auto_20160310_1245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='id',
        ),
        migrations.AlterField(
            model_name='customer',
            name='c_Address',
            field=models.CharField(max_length=100, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='c_Cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='历史消费'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='c_Name',
            field=models.CharField(max_length=20, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='m_Level',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Customer.Member', verbose_name='会员等级'),
        ),
        migrations.AlterField(
            model_name='member',
            name='m_Level',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='会员等级'),
        ),
    ]
