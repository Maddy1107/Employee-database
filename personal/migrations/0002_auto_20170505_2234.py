# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-05 17:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employment',
            name='Date_of_Resigning',
        ),
        migrations.RemoveField(
            model_name='employment',
            name='Last_working_day',
        ),
        migrations.RemoveField(
            model_name='employment',
            name='Location',
        ),
        migrations.RemoveField(
            model_name='employment',
            name='Transfer_date',
        ),
        migrations.RemoveField(
            model_name='employment',
            name='Transfer_to',
        ),
        migrations.RemoveField(
            model_name='employment',
            name='UAN_No',
        ),
    ]
