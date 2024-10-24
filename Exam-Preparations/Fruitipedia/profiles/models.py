from django.core.validators import MinLengthValidator
from django.db import models

from profiles.validators import StartsWithLetterValidator


# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
        validators=[
            MinLengthValidator(2),
            StartsWithLetterValidator()
        ]
    )

    last_name = models.CharField(
        max_length=35,
        validators=[
            MinLengthValidator(1),
            StartsWithLetterValidator()
        ]
    )

    email = models.EmailField(
        max_length=40
    )

    password = models.CharField(
        max_length=20,
        validators=[
            MinLengthValidator(8)
        ],
        help_text='*Password length requirements: 8 to 20 characters'
    )

    image_url = models.URLField(
        blank=True,
        null=True
    )

    age = models.IntegerField(
        blank=True,
        null=True,
        default=18
    )

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
