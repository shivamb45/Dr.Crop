# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 08:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_assist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submittedimage',
            name='path',
            field=models.TextField(blank=True, null=True),
        ),
    ]
