# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-01 04:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacation',
            name='year',
            field=models.CharField(default=2018, max_length=4),
            preserve_default=False,
        ),
    ]