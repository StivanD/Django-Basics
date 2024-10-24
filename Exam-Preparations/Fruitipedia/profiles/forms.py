from django import forms
from django.forms import PasswordInput, TextInput, EmailInput

from Fruitipedia.mixins import PlaceholderMixin
from profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        abstract=True
        widgets = {
            'first_name': TextInput(
                attrs={
                    'placeholder': 'First Name'
                }
            ),
            'last_name': TextInput(
                attrs={
                    'placeholder': 'Last Name'
                }
            ),
            'email': EmailInput(
                attrs={
                    'placeholder': 'Email'
                }
            ),
            'password': PasswordInput(
                attrs={
                    'placeholder': 'Password'
                }
            )
        }
        labels = {field: '' for field in ['first_name', 'last_name', 'email', 'password']}


class ProfileCreateForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        fields = ['first_name', 'last_name', 'email', 'password']


class ProfileEditForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        exclude = ('password', )