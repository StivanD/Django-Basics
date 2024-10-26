from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from recipes.choices import RecipeCuisineTypeChoice


# Create your models here.
class Recipe(models.Model):
    title = models.CharField(
        max_length=100,
        unique=True,
        validators=[
            MinLengthValidator(10)
        ],
        error_messages={
            'unique': 'We already have a recipe with the same title!'
        }
    )

    cuisine_type = models.CharField(
        max_length=7,
        choices=RecipeCuisineTypeChoice.choices
    )

    ingredients = models.TextField(
        help_text='Ingredients must be separated by a comma and space.'
    )

    instructions = models.TextField()

    cooking_time = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1)
        ],
        help_text='Provide the cooking time in minutes.'
    )

    image_url = models.URLField(
        blank=True,
        null=True
    )

    author = models.ForeignKey(
        to='profiles.Profile',
        on_delete=models.CASCADE,
        related_name='recipes'
    )

    def get_ingredients_list(self):
        return self.ingredients.split(', ')