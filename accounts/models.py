__author__ = 'mjeffrey'
from django.db import models
from django.db.models.signals import post_save
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from core.choices import US_STATES



class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female')
    )

    user = models.OneToOneField(User, editable=False, unique=True)
    gender = models.CharField(max_length=2, blank=True, choices=GENDER_CHOICES)
    birth_date = models.DateField(blank=True, null=True)
    school = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=2, choices=US_STATES)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='image/user', null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    courses = models.ManyToManyField('course.Course', blank=True, null=True, editable=False)
    video = models.FileField(help_text='Upload a video to introduce yourself',
                             upload_to='video/user',
                             blank=True, null=True)

    def __str__(self):
        if self.user.first_name == '':
            return self.user.username
        return u" ".join([self.user.first_name, self.user.last_name])

    def get_absolute_url(self):
        return reverse('user:view', kwargs={'slug': self.user.username})

    def enroll_in_course(self, course):
        self.courses.add(course)

    def unenroll_from_course(self, course):
        self.courses.remove(course)


def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_profile, sender=User)
