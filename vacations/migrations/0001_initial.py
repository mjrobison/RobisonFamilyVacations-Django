# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-19 02:48
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vacation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255)),
                ('month', models.SmallIntegerField(validators=[django.core.validators.MaxValueValidator(12, 'Must be number between 1 and 12'), django.core.validators.MinValueValidator(1, 'Must be a number between 1 and 12')])),
            ],
        ),
    ]
