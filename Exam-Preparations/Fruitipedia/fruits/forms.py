from django import forms
from django.forms import TextInput, URLInput, Textarea

from Fruitipedia.mixins import DisabledMixin
from fruits.models import Fruit


class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        exclude = ('owner', )


class FruitCreateForm(FruitBaseForm):
    class Meta(FruitBaseForm.Meta):
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Fruit Name'
                }
            ),
            'image_url': URLInput(
                attrs={
                    'placeholder': 'Fruit Image URL'
                }
            ),
            'description': Textarea(
                attrs={
                    'placeholder': 'Fruit Description'
                }
            ),
            'nutrition': Textarea(
                attrs={
                    'placeholder': 'Nutrition Info'
                }
            )
        }

        labels = {field: '' for field in ['name', 'image_url', 'description', 'nutrition']}


class FruitEditForm(FruitBaseForm):
    pass


class FruitDeleteForm(DisabledMixin, FruitBaseForm):
    class Meta(FruitBaseForm.Meta):
        exclude = ('nutrition', 'owner')

    disabled_fields = ['name', 'image_url', 'description']