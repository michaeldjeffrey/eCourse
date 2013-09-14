__author__ = 'mjeffrey'
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.template import RequestContext
from django.contrib.auth import login, authenticate, logout
from course.models import Course
from django.views.generic import TemplateView



# def index(request):
#     """ Return the homepage with the first 3 courses """
#     courses = Course.objects.get([1, 2, 3])
#     return render(request, 'core/index.html', courses)

class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['courses'] = Course.objects.all()[:3]
        return context


def mylogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Success
                return HttpResponseRedirect('/')
            else:
                # disabled account
                # return HttpResponseRedirect(reverse())
                return direct_to_template(request, 'invalid_login.html')

def mylogout(request):
    logout(request)
    return direct_to_template(request, 'logged_out.html')
