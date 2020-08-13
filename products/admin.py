from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'price',
        'stock',
        'seller',
        'created_at',
    )
    search_fields = (
        'name',
    )
    
    
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'writer',
        'product',
        'rating',
    )
    search_fields = (
        'writer',
    )
