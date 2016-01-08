from django.contrib import admin
from .models import *

class VoteInLine(admin.StackedInline):
    model = Answer
    extra = 2

class VoteAdmin(admin.ModelAdmin):
        fields = ['question', 'date', 'is_single']
        inlines = [VoteInLine]
        list_filter = ['date']

admin.site.register(Vote, VoteAdmin)