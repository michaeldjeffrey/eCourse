__author__ = 'mjeffrey'
from django.db import models
from django.core.urlresolvers import reverse


class User(models.Model):
    """ Base user model. """
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    signup_date = models.DateTimeField(auto_now_add=True)
    last_logged_in = models.DateTimeField(auto_now=True)
    website = models.CharField(max_length=100, blank=True)

