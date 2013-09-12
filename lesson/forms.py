__author__ = 'mjeffrey'
from django import forms
from lesson.models import Lesson, Reference, Image, Video
from django.forms.formsets import formset_factory
from django.forms.models import inlineformset_factory, modelformset_factory

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson

class ReferenceForm(forms.ModelForm):
    class Meta:
        model = Reference

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video


ReferenceInlineFormset = inlineformset_factory(Lesson, Reference, extra=2)
ImageInlineFormset = inlineformset_factory(Lesson, Image, extra=2)
VideoInlineFormset = inlineformset_factory(Lesson, Video, extra=2)
