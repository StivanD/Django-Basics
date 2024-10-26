import re

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.text import slugify


@deconstructible
class AlphaNumericValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if not value:
            self.__message = 'Username must contain only letters, digits, and underscores!'
        else:
            self.__message = value

    def __call__(self, value: str, *args, **kwargs):
        if not re.match(r'^[a-zA-Z0-9_]+$', value):
            raise ValidationError(self.message)
