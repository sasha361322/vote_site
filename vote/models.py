from __future__ import unicode_literals

from django.db import models

class Vote(models.Model):
    class Meta:
        db_table = 'vote'
    question = models.CharField(max_length=200)
    date = models.DateTimeField()
    count = models.IntegerField()
    is_single = models.BooleanField(default=True)


class Answer(models.Model):
    class Meta:
        db_table = 'answer'
    text = models.CharField(max_length=200)
    count = models.IntegerField(default=0)
    number = models.IntegerField()
    answer_vote = models.ForeignKey(Vote, null=True)
