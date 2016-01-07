from django.conf.urls import patterns, include, url
from django.conf.urls import url
from . import views

urlpatterns = [
      url(r'^$', 'vote.views.votes'),
      url(r'^vote/get/(?P<vote_id>\d+)$', 'vote.views.vote'),
      url(r'^vote/addanswer/(?P<description_id>\d+)/$', 'vote.views.addanswer'),
      url(r'^vote/addvote/$', 'vote.views.addvote'),
      url(r'^vote/addanswers/(?P<vote_id>\d+)/(?P<n>\d+)$', 'vote.views.addanswers'),
    ]