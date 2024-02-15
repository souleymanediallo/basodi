from django.contrib import admin
from .models import Color, Condition, Category, Article, SubCategory, Size, Tag, MainCategory


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['ordering', 'name', 'category', 'subcategory', 'price', 'color', 'condition']
    list_display_links = ['name']
    list_editable = ['ordering', 'category', 'subcategory', 'price', 'color', 'condition']


admin.site.register(Article, ArticleAdmin)

class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ['ordering', 'name']
    list_display_links = ['name', 'ordering']

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


class ColorAdmin(admin.ModelAdmin):
    list_display = ['ordering', 'name']
    list_display_links = ['name']
    list_editable = ['ordering']

admin.site.register(Color, ColorAdmin)



class ConditionAdmin(admin.ModelAdmin):
    list_display = ['ordering', 'name']
    list_display_links = ['name']
    list_editable = ['ordering']

admin.site.register(Condition, ConditionAdmin)

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['ordering', 'name', 'category']
    list_display_links = ['name']
    list_editable = ['ordering']

    # choisir catrgorie parent
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            kwargs["queryset"] = Category.objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



class SizeAdmin(admin.ModelAdmin):
    list_display = ['ordering', 'name', 'type_choice']
    list_display_links = ['name']
    list_editable = [ 'ordering']

admin.site.register(Size, SizeAdmin)



class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'ordering', 'name']
    list_editable = ['ordering']

admin.site.register(Tag, TagAdmin)