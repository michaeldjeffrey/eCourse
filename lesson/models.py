from django.db import models
from course.models import Course
from datetime import datetime
from django.core.urlresolvers import reverse


# Create your models here.
class Lesson(models.Model):
    course = models.ForeignKey(Course)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(default=datetime.now())
    due_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lesson:view', kwargs={"pk": self.id})

    def delete(self, using=None):
        self.reference_set.all().delete()
        self.image_set.all().delete()
        super(Lesson, self).delete()


class Reference(models.Model):
    lesson = models.ForeignKey(Lesson)
    title = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.title


class Image(models.Model):
    lesson = models.ForeignKey(Lesson)
    # reference = models.ForeignKey(Reference, blank=True, null=True)
    image = models.ImageField(upload_to='image/lesson')


class Video(models.Model):
    lesson = models.ForeignKey(Lesson)
    video = models.FileField(upload_to='video/lesson')
