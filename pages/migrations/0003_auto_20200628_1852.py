# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-28 22:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20200529_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='css',
            field=models.TextField(blank=True, verbose_name=b'CSS'),
        ),
    ]
