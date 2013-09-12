from django.db import models
from accounts.models import UserProfile
from django.core.urlresolvers import reverse
from core.choices import CLASS_SUBJECTS
from datetime import datetime


class Course(models.Model):
    """
    A class.
    Created by one teacher.
    Has many students.
    Has many lessons.
    """
    title = models.CharField(max_length=20)
    subject = models.CharField(max_length=20, choices=CLASS_SUBJECTS)
    description = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField(default=datetime.now())
    end_date = models.DateField(default=datetime.now())
    description = models.TextField()
    teacher = models.ForeignKey(UserProfile)
    image = models.ImageField(upload_to='image/course', blank=True, null=True)
    # URL for video of class lecture
    video = models.FileField(help_text='Intro video to the course', upload_to='video/course',
                             blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course:view', kwargs={"pk": self.id})

    def course_duration(self):
        """ how many weeks is the course. """
        weeks = self.end_date - self.start_date
        return weeks.days / 7

    def num_of_students(self):
        """ number of students enrolled in the class. """
        self.students.count()

    def lesson_count(self):
        """ number of lessons in the course. """
        self.less


# class CourseImage(models.Model):
#     course = models.ForeignKey(Course, related_name='images')
#     image = models.ImageField(upload_to='course')
