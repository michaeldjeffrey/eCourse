__author__ = 'mjeffrey'
from django import template
from django.template.loader import render_to_string

register = template.Library()

@register.filter(name='file_field')
def file_field(field):
    return render_to_string('templatetags/file_field.html', {
        'field': field,
    })

@register.filter(name='image_field')
def image_field(field):
    return render_to_string('templatetags/image_field.html', {
        'field': field,
    })
