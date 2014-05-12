__author__ = 'mjeffrey'
from django import forms
from django.forms.fields import DateField, CharField
from django.forms.widgets import Textarea
from django.forms.extras.widgets import SelectDateWidget
# from django.forms.models import inlineformset_factory
from accounts.models import UserProfile
from django.contrib.admin.widgets import AdminFileWidget


from course.models import Course
# from lesson.models import Lesson


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        exclude = ('teacher',)

    def clean(self):
        return self.cleaned_data

# CourseLessonFormset = inlineformset_factory(
#     CourseForm, Lesson,
# )
