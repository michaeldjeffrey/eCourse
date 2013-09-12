__author__ = 'mjeffrey'
from django.conf.urls import *
from django.views.generic import DetailView, ListView
from views import *

urlpatterns = patterns('',
    url(r'^$', ListCourseView.as_view(), name='list'),
    url(r'^new/$', CreateCourseView.as_view(), name='new'),
    url(r'^(?P<pk>\d+)/$', CourseView.as_view(), name='view'),
    url(r'^(?P<pk>\d+)/edit/$', UpdateCourseView.as_view(), name='edit'),
    url(r'^(?P<pk>\d+)/delete/$', DeleteCourseView.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)/enroll/$', enroll, name='enroll'),
    url(r'^(?P<pk>\d+)/unenroll/$', unenroll, name='unenroll'),
)

