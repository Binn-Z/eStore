# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-09 13:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Customer', '0001_initial'),
        ('Goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_Date', models.DateField()),
                ('c_Content', models.TextField()),
                ('c_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.Customer')),
                ('g_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Goods.Goods')),
            ],
        ),
    ]
