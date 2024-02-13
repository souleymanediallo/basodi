from django.contrib import admin
from .models import Color, Condition, Category, Article, SubCategory, Size, Tag, MainCategory


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['ordering', 'name', 'category', 'subcategory', 'price', 'color', 'condition']


class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ['ordering', 'name']

admin.site.register(MainCategory, MainCategoryAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['ordering', 'main_category', 'name']
    # moidier les noms des colonnes
    list_display_links = ['main_category']
    list_editable = ['name']
    # choisir catrgorie parent
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "main_category":
            kwargs["queryset"] = MainCategory.objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # choisir catrgorie parent





admin.site.register(Category, CategoryAdmin)

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['id', 'ordering', 'name']


@admin.register(Condition)
class ConditionAdmin(admin.ModelAdmin):
    list_display = ['id', 'ordering', 'name']


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'ordering', 'name', 'category']

    # choisir catrgorie parent
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            kwargs["queryset"] = Category.objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['id', 'ordering', 'name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'ordering', 'name']
