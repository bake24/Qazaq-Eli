from django import template
from cityapp.models import *

register = template.Library()

@register.simple_tag(name = 'getcats')
def get_categories(filter = None):
    if not filter:
        return City.objects.all()
    else:
        return City.objects.filter(pk=filter)


@register.inclusion_tag('cityapp/list_categories.html')
def show_categories(sort = None, cat_selected = 0):
    if not sort:
       cats =  City.objects.all()
    else:
        cats = City.objects.order_by(sort)
    return {'cats' : cats, 'cat_selected': cat_selected}