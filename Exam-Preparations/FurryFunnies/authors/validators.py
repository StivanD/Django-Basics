from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class ContainsOnlyLettersValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = 'Your name must contain letters only!'
        else:
            self.__message = value

    def __call__(self, value: str, *args, **kwargs):
        if not value.isalpha():
            raise ValidationError(self.message)


@deconstructible
class HasExactlySixDigitsValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = 'Your passcode must be exactly 6 digits!'
        else:
            self.__message = value

    def __call__(self, value: str, *args, **kwargs):
        if not (len(value) == 6 and value.isdigit()):
            raise ValidationError(self.message)
