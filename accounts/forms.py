__author__ = 'mjeffrey'

from django import forms
from models import UserProfile
from django.contrib.admin import widgets
from django.core.urlresolvers import reverse, reverse_lazy



class UserProfileForm(forms.ModelForm):

    birth_date = forms.DateField(widget=widgets.AdminDateWidget())

    # username = forms.CharField(label='Username', max_length=30)
    first_name = forms.CharField(label='First name', max_length=30)
    last_name = forms.CharField(label='Last name', max_length=30)

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        # self.fields['username'].initial = self.instance.user.username
        self.fields['first_name'].initial = self.instance.user.first_name
        self.fields['first_name'].required = False
        self.fields['last_name'].initial = self.instance.user.last_name
        self.fields['last_name'].required = False

    def save(self, *args, **kwargs):
        super(UserProfileForm, self).save(*args, **kwargs)
        # self.instance.user.username = self.cleaned_data.get('username')
        self.instance.user.first_name = self.cleaned_data.get('first_name')
        self.instance.user.last_name = self.cleaned_data.get('last_name')
        self.instance.user.save()

    def get_success_url(self):
        return reverse('user:view', kwargs={'slug': self.request.user})


    class Meta:
        model = UserProfile
        # exclude = 'user'

