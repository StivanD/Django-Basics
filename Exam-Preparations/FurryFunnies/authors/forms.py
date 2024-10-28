from django import forms
from django.forms import PasswordInput, TextInput, NumberInput

from authors.models import Author


class AuthorBaseForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        widgets = {
            'first_name': TextInput(
                attrs={
                    'placeholder': 'Enter your first name...',
                    'label': 'First Name:'
                }
            ),
            'last_name': TextInput(
                attrs={
                    'placeholder': 'Enter your last name...',
                    'label': 'Last Name:'
                }
            ),
            'passcode': PasswordInput(
                attrs={
                    'placeholder': 'Enter 6 digits...',
                    'label': 'Passcode:'
                }
            ),
            'pets_number': NumberInput(
                attrs={
                    'placeholder': 'Enter the number of your pets...',
                    'label': 'Pets Number:'
                }
            )
        }

        # labels = {
        #     'last_name': 'Last Name:',
        #     'passcode': 'Passcode:',
        #     'pets_number': 'Pets Number:'
        # }


class AuthorCreateForm(AuthorBaseForm):
    class Meta(AuthorBaseForm.Meta):
        fields = ['first_name', 'last_name', 'passcode', 'pets_number']


class AuthorEditForm(AuthorBaseForm):
    class Meta(AuthorBaseForm.Meta):
        exclude = ('passcode',)