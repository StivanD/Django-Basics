from django import forms
from django.forms import PasswordInput

from profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'password': PasswordInput()
        }


class ProfileCreateForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        exclude = ('first_name', 'last_name', 'profile_picture')


class ProfileEditForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        widgets = None
