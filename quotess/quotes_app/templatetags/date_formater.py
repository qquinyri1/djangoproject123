from datetime import datetime

from django import template

register = template.Library()


def format_date(date_object):
    return date_object.strftime('%B %d, %Y')


register.filter('date', format_date)