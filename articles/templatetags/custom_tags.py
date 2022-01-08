from django import template
from articles.models import Category, SubCategory

register = template.Library()


@register.simple_tag(name='categories')
def all_categories():
    return Category.objects.all()


@register.simple_tag(name='subcategories')
def all_subcategories():
    return SubCategory.objects.all()
