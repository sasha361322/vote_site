#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Vote(models.Model):
    class Meta:
        db_table = 'vote'
    question = models.CharField(max_length=200)
    date = models.DateTimeField()
    is_single = models.BooleanField(default=True)


class Answer(models.Model):
    class Meta:
        db_table = 'answer'
    text = models.CharField(max_length=200, verbose_name="Вариант ответа")
    count = models.IntegerField(default=0)
    answer_vote = models.ForeignKey(Vote, null=True)
