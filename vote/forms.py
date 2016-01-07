from django.forms import *
from .models import Vote, Answer

class VoteForm(ModelForm):
    class Meta:
        model = Vote
        fields = ['question', 'count', 'date', 'is_single']

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['text']