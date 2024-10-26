from django.core.validators import MinLengthValidator
from django.db import models

from profiles.validators import StartsWithCapitalLetterValidator


# Create your models here.
class Profile(models.Model):
    nickname = models.CharField(
        max_length=20,
        validators=[
            MinLengthValidator(2, 'Nickname must be at least 2 chars long!')
        ]
    )

    first_name = models.CharField(
        max_length=30,
        validators=[
            StartsWithCapitalLetterValidator()
        ]
    )

    last_name = models.CharField(
        max_length=30,
        validators=[
            StartsWithCapitalLetterValidator()
        ]
    )

    chef = models.BooleanField(
        default=False
    )

    bio = models.TextField(
        blank=True,
        null=True
    )

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
