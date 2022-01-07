from django.contrib import admin
from .models import Color, Condition, Category, Article, SubCategory, Size, Tag

# Register your models here.
admin.site.register(Color)
admin.site.register(Condition)
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(SubCategory)
admin.site.register(Size)
admin.site.register(Tag)