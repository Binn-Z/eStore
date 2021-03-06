# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-10 04:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['c_Name'], 'verbose_name': '顾客', 'verbose_name_plural': '顾客'},
        ),
        migrations.AlterModelOptions(
            name='member',
            options={'ordering': ['m_Level'], 'verbose_name': '会员等级', 'verbose_name_plural': '会员等级'},
        ),
        migrations.AlterField(
            model_name='customer',
            name='c_Address',
            field=models.CharField(max_length=100, verbose_name='顾客地址'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='c_Cost',
            field=models.DecimalField(decimal_places=2, max_digits=12, verbose_name='历史消费'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='c_Name',
            field=models.CharField(max_length=20, verbose_name='顾客姓名'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='c_Password',
            field=models.CharField(max_length=20, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='c_Phone',
            field=models.CharField(max_length=20, unique=True, verbose_name='手机号码'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='m_Level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.Member', verbose_name='会员等级'),
        ),
        migrations.AlterField(
            model_name='member',
            name='m_Description',
            field=models.CharField(blank=True, max_length=100, verbose_name='等级描述'),
        ),
        migrations.AlterField(
            model_name='member',
            name='m_Discount',
            field=models.FloatField(verbose_name='优惠'),
        ),
        migrations.AlterField(
            model_name='member',
            name='m_Level',
            field=models.IntegerField(verbose_name='会员等级'),
        ),
    ]
