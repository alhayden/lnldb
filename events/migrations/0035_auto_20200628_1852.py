# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-28 22:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0034_auto_20200425_2033'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fund',
            options={'permissions': (('manage_fund', 'View a fund'),)},
        ),
        migrations.AlterModelOptions(
            name='posteventsurvey',
            options={'ordering': ['event', 'person'], 'permissions': (('view_posteventsurveyresults', 'View post-event survey results'),)},
        ),
    ]