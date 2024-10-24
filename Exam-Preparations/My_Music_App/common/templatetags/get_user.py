from django import template

from My_Music_App.utils import get_user_obj

register = template.Library()


@register.simple_tag()
def get_user():
    return get_user_obj()