from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.decorators import login_required as auth
from core import settings
from views import IndexView

from accounts.views import AccountDetailView, UserProfileEditView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^course/', include('course.urls', namespace='course')),
    url(r'^lesson/', include('lesson.urls', namespace='lesson')),
    url(r'^user/', include('accounts.urls', namespace='user')),
)

urlpatterns += staticfiles_urlpatterns()

urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True})
)


# GO HERE
# django-registration.readthedocs.org/en/latest/quickstart.html
