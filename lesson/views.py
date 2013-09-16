__author__ = 'mjeffrey'
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.core.urlresolvers import reverse
from lesson.models import Lesson
from lesson.forms import LessonForm, ReferenceInlineFormset, ImageInlineFormset, VideoInlineFormset
from django.forms.formsets import BaseFormSet, formset_factory, ValidationError
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from core.utils import AuthenticationMixin


class ListLessonView(AuthenticationMixin, ListView):
    """ List all the lessons in the db. """
    model = Lesson


class UpdateLessonView(UpdateView):
    model = Lesson
    form_class = LessonForm

    def get_success_url(self):
        return reverse('lesson:list')


    def get_context_data(self, **kwargs):
        context = super(UpdateLessonView, self).get_context_data(**kwargs)
        context['action'] = reverse('lesson:edit', kwargs={'pk': self.get_object().id})
        instance = None
        if self.request.POST:
            context['form'] = LessonForm(self.request.POST, instance=self.object)
            context['image'] = ImageInlineFormset(self.request.POST, self.request.FILES,instance=self.object)
            context['video'] = VideoInlineFormset(self.request.POST, self.request.FILES,instance=self.object)
            context['reference'] = ReferenceInlineFormset(self.request.POST, instance=self.object)
        else:
            context['form'] = LessonForm(instance=self.object)
            context['image'] = ImageInlineFormset(instance=self.object)
            context['video'] = VideoInlineFormset(instance=self.object)
            context['reference'] = ReferenceInlineFormset(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        form = context['form']
        image = context['image']
        video = context['video']
        reference = context['reference']
        if form.is_valid():
            self.object = form.save()
            if reference.is_valid() and image.is_valid() and video.is_valid():
                reference.instance = self.object
                reference.save()
                image.instance = self.object
                image.save()
                video.instance = self.object
                video.save()
            return redirect(self.object.course.get_absolute_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class CreateLessonView(AuthenticationMixin, CreateView):
    """ Create a new Contact. """
    model = Lesson
    form_class = LessonForm
    success_url = '/course/'

    def get_success_url(self):
        return reverse('lesson:list')

    def get_context_data(self, **kwargs):
        context = super(CreateLessonView, self).get_context_data(**kwargs)
        instance = None
        if self.request.POST:
            context['form'] = LessonForm(self.request.POST, instance=instance)
            context['image'] = ImageInlineFormset(self.request.POST, self.request.FILES, instance=instance)
            context['video'] = VideoInlineFormset(self.request.POST, self.request.FILES, instance=instance)
            context['reference'] = ReferenceInlineFormset(self.request.POST, instance=instance)
        else:
            context['form'] = LessonForm(instance=instance)
            context['image'] = ImageInlineFormset(instance=instance)
            context['video'] = VideoInlineFormset(instance=instance)
            context['reference'] = ReferenceInlineFormset(instance=instance)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        form = context['form']
        image = context['image']
        video = context['video']
        reference = context['reference']
        if form.is_valid():
            self.object = form.save()
            if reference.is_valid() and image.is_valid() and video.is_valid():
                reference.instance = self.object
                reference.save()
                image.instance = self.object
                image.save()
                video.instance = self.object
                video.save()
            return redirect(self.object.course.get_absolute_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))



    # model = Lesson
    # form_class = LessonForm
    #
    # def get_context_data(self, **kwargs):
    #     context = super(CreateLessonView, self).get_context_data(**kwargs)
    #     if self.request.POST:
    #         context['formset'] = ReferenceFormset(self.request.POST)
    #     else:
    #         context['formset'] = ReferenceFormset()
    #     return context
    #
    # def get_success_url(self):
    #     return reverse('lesson:list')
    #
    # def form_valid(self, form):
    #     object = form.save(commit=False)
    #     object.teacher = self.request.user.userprofile
    #     object.save()
    #     return super(CreateLessonView, self).form_valid(form)
    #
    # def get_form_kwargs(self):
    #     kwargs = super(CreateLessonView, self).get_form_kwargs()
    #     kwargs.update({'user': self.request.user})
    #     return kwargs
    #
    # def get_context_data(self, **kwargs):
    #     context = super(CreateLessonView, self).get_context_data(**kwargs)
    #     context['action'] = reverse('lesson:new')
    #     return context


# class UpdateCourseView(AuthenticationMixin, UpdateView):
#     """ Update an existing Contact. """
#     model = Course
#     form_class = CourseForm
#
#     def get_success_url(self):
#         return reverse('course:list')
#
#     def get_context_data(self, **kwargs):
#         context = super(UpdateCourseView, self).get_context_data(**kwargs)
#         context['action'] = reverse('course:edit', kwargs={'pk': self.get_object().id})
#         return context
#
#
class DeleteLessonView(AuthenticationMixin, DeleteView):
    """ Delete the current contact. """
    model = Lesson

    def get_success_url(self):
        return reverse('lesson:list')

    def get_context_data(self, **kwargs):
        context = super(DeleteLessonView, self).get_context_data(**kwargs)
        context['action'] = reverse('lesson:delete', kwargs={'pk': self.get_object().id})
        return context
#
#
class LessonView(AuthenticationMixin, DetailView):
    """ View the details of the current contact. """
    model = Lesson
#
#
# class EditCourseLessonView(UpdateView):
#     template_name = 'course/edit_lesson.html'
#     model = Course
#     form_class = CourseLessonFormset
#
#     def get_success_url(self):
#         return self.get_object().get_absolute_url()
