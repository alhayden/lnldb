# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-27 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0005_auto_20200826_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='MacOSApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('identifier', models.CharField(help_text='Homebrew Identifier', max_length=64)),
                ('version', models.CharField(blank=True, max_length=36, null=True)),
                ('developer', models.CharField(blank=True, max_length=64, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('update_available', models.BooleanField(blank=True, default=False)),
                ('installed', models.ManyToManyField(blank=True, related_name='apps_installed', to='devices.Laptop')),
                ('pending_install', models.ManyToManyField(blank=True, related_name='apps_pending', to='devices.Laptop')),
                ('pending_removal', models.ManyToManyField(blank=True, related_name='apps_remove', to='devices.Laptop')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'managed app',
                'permissions': (('view_apps', 'View managed laptop applications'), ('add_apps', 'Add apps to library'), ('manage_apps', 'Manage the app library')),
            },
        ),
    ]
