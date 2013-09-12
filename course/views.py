__author__ = 'mjeffrey'
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.core.urlresolvers import reverse
from course.models import Course
from course.forms import CourseForm
from core.utils import AuthenticationMixin
from django.http import HttpResponseRedirect


class ListCourseView(ListView):
    """ List all the contacts in the db. """
    model = Course


class CreateCourseView(AuthenticationMixin, CreateView):
    """ Create a new Contact. """
    model = Course
    form_class = CourseForm


    def get_success_url(self):
        return reverse('course:list')

    def form_valid(self, form):
        object = form.save(commit=False)
        object.teacher = self.request.user.userprofile
        object.save()
        return super(CreateCourseView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateCourseView, self).get_context_data(**kwargs)
        context['action'] = reverse('course:new')
        return context


class UpdateCourseView(UpdateView):
    """ Update an existing Contact. """
    model = Course
    form_class = CourseForm

    def get_success_url(self):
        return reverse('course:list')

    def get_context_data(self, **kwargs):
        context = super(UpdateCourseView, self).get_context_data(**kwargs)
        context['action'] = reverse('course:edit', kwargs={'pk': self.get_object().id})
        return context


class DeleteCourseView(DeleteView):
    """ Delete the current contact. """
    model = Course

    def get_success_url(self):
        return reverse('course:list')

    def get_context_data(self, **kwargs):
        context = super(DeleteCourseView, self).get_context_data(**kwargs)
        context['action'] = reverse('course:delete', kwargs={'pk': self.get_object().id})
        return context


class CourseView(AuthenticationMixin, DetailView):
    """ View the details of the current contact. """
    model = Course


def enroll(request, pk):
    course = pk
    request.user.userprofile.enroll_in_course(course)
    return HttpResponseRedirect('/')

def unenroll(request, pk):
    course = pk
    request.user.userprofile.unenroll_from_course(course)
    return HttpResponseRedirect('/')


#
#
# class EditCourseLessonView(UpdateView):
#     template_name = 'course/edit_lesson.html'
#     model = Course
#     form_class = CourseLessonFormset
#
#     def get_success_url(self):
#         return self.get_object().get_absolute_url()
