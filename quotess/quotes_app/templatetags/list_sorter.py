from datetime import datetime

from django import template
from ..models import Tag

register = template.Library()


def sort_list(_list):
    if type(_list[0]) is Tag:
        return sorted(_list, key=lambda x: x.name)
    return sorted(_list, key=lambda x: x.fullname)


register.filter('sort', sort_list)