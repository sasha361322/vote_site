from django.conf.urls import patterns, include, url
from django.conf.urls import url
from . import views

urlpatterns = [
      url(r'^login/', 'loginsys.views.login'),
      url(r'^logout/', 'loginsys.views.logout'),
    ]