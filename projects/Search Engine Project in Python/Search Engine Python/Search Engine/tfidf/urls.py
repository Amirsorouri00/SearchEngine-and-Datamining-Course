'''
Created on Mar 23, 2013

@author: daoxuandung
'''
from django.conf.urls import url
from tfidf import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^term/autocomplete/$', views.term_autocomplete, name='autocomplete')
]
