__author__ = 'mjeffrey'
import os
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import ImproperlyConfigured


PATH_HANDLER_WARNING = 'upload_path_handler must be provided a model: {} and type: {}'


class AuthenticationMixin(object):
    permission_required = None

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        dispatch = super(AuthenticationMixin, self).dispatch
        return dispatch(request, *args, **kwargs)

    def has_permission(self, user):
        return True

