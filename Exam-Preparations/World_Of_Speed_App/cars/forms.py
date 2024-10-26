from django import forms
from django.forms import URLInput

from WorldOfSpeed.mixins import ReadOnlyMixin
from cars.models import Car


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ('owner', )
        widgets = {
            'image_url': URLInput(
                attrs={
                    'placeholder': 'https://...'
                }
            )
        }


class CarCreateForm(CarBaseForm):
    pass


class CarEditForm(CarBaseForm):
    pass


class CarDeleteForm(ReadOnlyMixin, CarBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'type' in self.fields:
            self.fields['type'].disabled = True
