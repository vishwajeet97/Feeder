# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0019_auto_20161103_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.ManyToManyField(blank=True, to='backend.Course'),
        ),
    ]
