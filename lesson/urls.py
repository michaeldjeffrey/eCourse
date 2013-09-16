__author__ = 'mjeffrey'
from django.conf.urls import *
from django.views.generic import DetailView, ListView
from views import *

urlpatterns = patterns('',
    url(r'^$', ListLessonView.as_view(), name='list'),
    url(r'^new/$', CreateLessonView.as_view(), name='new'),
    url(r'^(?P<pk>\d+)/$', LessonView.as_view(), name='view'),
    url(r'^(?P<pk>\d+)/edit$', UpdateLessonView.as_view(), name='edit'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteLessonView.as_view(), name='delete'),
)
