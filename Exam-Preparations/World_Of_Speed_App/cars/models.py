from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from cars.choices import CarTypeChoice
from cars.validators import ValidYearValidator


# Create your models here.
class Car(models.Model):
    type = models.CharField(
        max_length=10,
        choices=CarTypeChoice.choices
    )

    model = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(1)
        ]
    )

    year = models.IntegerField(
        validators=[
            ValidYearValidator()
        ]
    )

    image_url = models.URLField(
        unique=True,
        error_messages={
            'unique': 'This image URL is already in use! Provide a new one.'
        }
    )

    price = models.FloatField(
        validators=[
            MinValueValidator(1.0)
        ]
    )

    owner = models.ForeignKey(
        to='profiles.Profile',
        on_delete=models.CASCADE,
        related_name='cars'
    )