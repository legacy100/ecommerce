from django.contrib import admin
from .models import Product, Category

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
# the admin site will display the name of the category instead of the id
    list_display = ['name', 'slug']
# the prepopulated_fields dictionary is used to automatically fill in the slug field with the name of the category when the category is created.
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'price', 'in_stock', 'created', 'updated']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('title',)}

# @admin.deactivate('Groups')