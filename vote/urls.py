from django.conf.urls import patterns, include, url
from django.conf.urls import url
from . import views

urlpatterns = [
      url(r'^vote/get/(?P<vote_id>\d+)/$', 'vote.views.vote'),
      url(r'^vote/addanswer/(?P<vote_id>\d+)/(?P<answer_id>\d+)/$', 'vote.views.addanswer'),
      url(r'^vote/addvote/$', 'vote.views.addvote'),
      url(r'^vote/addanswers/(?P<vote_id>\d+)/$', 'vote.views.addanswers'),
      url(r'^page/(\d+)/$', 'vote.views.votes'),
      url(r'^vote/get/(\d)?(?P<str>)/$', 'vote.views.test'),
      url(r'^', 'vote.views.votes'),
    ]