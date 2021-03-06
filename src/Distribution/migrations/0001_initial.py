# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-09 13:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deliveryman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_Name', models.CharField(max_length=20)),
                ('p_Sex', models.BooleanField()),
                ('p_Phone', models.CharField(max_length=20)),
                ('p_Num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Distribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_Date', models.DateField(auto_now=True)),
                ('o_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Orders.Orders')),
                ('p_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Distribution.Deliveryman')),
            ],
        ),
    ]
