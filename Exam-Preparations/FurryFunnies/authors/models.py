from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from authors.validators import ContainsOnlyLettersValidator, HasExactlySixDigitsValidator


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(
        max_length=40,
        validators=[
            MinLengthValidator(4),
            ContainsOnlyLettersValidator()
        ]
    )

    last_name = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(2),
            ContainsOnlyLettersValidator()
        ]
    )

    passcode = models.CharField(
        max_length=6,
        validators=[
            HasExactlySixDigitsValidator()
        ],
        help_text='Your passcode must be a combination of 6 digits'
    )

    pets_number = models.SmallIntegerField(
        validators=[
            MinValueValidator(0)
        ]
    )

    info = models.TextField(
        blank=True,
        null=True
    )

    image_url = models.URLField(
        blank=True,
        null=True
    )

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'