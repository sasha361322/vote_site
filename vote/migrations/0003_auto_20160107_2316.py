# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-07 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0002_answer_answer_vote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='vote',
            name='is_single',
            field=models.BooleanField(default=True),
        ),
    ]