# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-13 02:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyathalon_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
