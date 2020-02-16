# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-15 22:21
from __future__ import unicode_literals

from django.db import migrations, models
import inventory.models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_auto_20181021_2135'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentUserGuide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=inventory.models.guide_file_name)),
                ('name', models.CharField(max_length=50)),
                ('date_modified', models.DateTimeField(auto_now_add=True)),
                ('tmpl', models.BooleanField(default=False)),
                ('datasheet', models.BooleanField(default=False)),
            ],
            options={
                'permissions': (('edit_guides', 'Upload or edit User Guides'), ('view_guides', 'View User Guides')),
            },
        ),
    ]