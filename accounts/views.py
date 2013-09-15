# Create your views here.
from django.views.generic import DetailView, UpdateView, ListView
from django.contrib.auth.models import User
from models import UserProfile
from forms import UserProfileForm
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse, reverse_lazy


class ListAccountView(ListView):
    model = UserProfile
    template_name = 'accounts/account_list.html'


class AccountDetailView(DetailView):
    model = get_user_model()
    slug_field = 'username'
    template_name = 'accounts/account_detail.html'

    def get_object(self, queryset=None):
        user = super(AccountDetailView, self).get_object(queryset)
        UserProfile.objects.get_or_create(user=user)
        return user


class UserProfileEditView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'accounts/account_form.html'


    def get_object(self, queryset=None):
        return UserProfile.objects.get_or_create(user=self.request.user)[0]

    def get_success_url(self):
        return reverse('user:view', kwargs={'slug': self.request.user})
