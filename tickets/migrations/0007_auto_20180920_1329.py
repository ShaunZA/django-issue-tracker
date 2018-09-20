# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-09-20 13:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_ticket_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='created_by',
            field=models.CharField(default=' ', editable=False, max_length=32),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='title',
            field=models.CharField(default=' ', max_length=64),
        ),
    ]
