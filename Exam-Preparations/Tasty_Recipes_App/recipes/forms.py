from django import forms
from django.forms import TextInput, URLInput

from TastyRecipes.mixins import ReadOnlyMixin
from recipes.models import Recipe


class RecipeBaseForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ('author', )


class RecipeCreateForm(forms.ModelForm):
    class Meta(RecipeBaseForm.Meta):
        widgets = {
            'ingredients': TextInput(
                attrs={
                    'placeholder': 'ingredient1, ingredient2, ...'
                }
            ),
            'instructions': TextInput(
                attrs={
                    'placeholder': 'Enter detailed instructions here...'
                }
            ),
            'image_url': URLInput(
                attrs={
                    'placeholder': 'Optional image URL here...'
                }
            )
        }


class RecipeEditForm(RecipeBaseForm):
    pass


class RecipeDeleteForm(ReadOnlyMixin, RecipeBaseForm):
    read_only_fields = ['title', 'cuisine_type', 'ingredients', 'instructions', 'cooking_time', 'image_url']
