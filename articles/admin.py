from django.contrib import admin
from .models import Color, Condition, Category, Article, SubCategory, Size, Tag


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['ordering', 'name', 'category', 'subcategory', 'price', 'color', 'condition']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'ordering', 'name']


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['id', 'ordering', 'name']


@admin.register(Condition)
class ConditionAdmin(admin.ModelAdmin):
    list_display = ['id', 'ordering', 'name']


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'ordering', 'name']


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['id', 'ordering', 'name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'ordering', 'name']
