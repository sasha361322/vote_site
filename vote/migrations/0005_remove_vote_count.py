# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-08 18:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0004_remove_answer_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='count',
        ),
    ]