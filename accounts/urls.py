__author__ = 'mjeffrey'
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required as auth

from accounts.views import AccountDetailView, UserProfileEditView

urlpatterns = patterns('',
    url(r'^(?P<slug>\w+)/$', AccountDetailView.as_view(), name='view'),
    url(r'^(?P<slug>\w+)/edit/$', auth(UserProfileEditView.as_view()), name='edit'),
)
