# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-11-03 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20201103_0900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='id',
        ),
        migrations.AlterField(
            model_name='booking',
            name='uuid',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]
