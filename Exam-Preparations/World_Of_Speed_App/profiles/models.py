from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.db.models import Sum

from profiles.validators import AlphaNumericValidator


# Create your models here.
class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(3, 'Username must be at least 3 chars long!'),
            AlphaNumericValidator()
        ]
    )

    email = models.EmailField()

    age = models.IntegerField(
        validators=[
            MinValueValidator(21)
        ],
        help_text='Age requirement: 21 years and above.'
    )

    password = models.CharField(
        max_length=20
    )

    first_name = models.CharField(
        max_length=25,
        blank=True,
        null=True
    )

    last_name = models.CharField(
        max_length=25,
        blank=True,
        null=True
    )

    profile_picture = models.URLField(
        blank=True,
        null=True
    )

    @property
    def cars_total(self):
        return self.cars.aggregate(Sum('price', default=0))['price__sum']