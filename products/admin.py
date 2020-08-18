from django.contrib import admin
from .models import *

# Product(상품)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # 목록에 표시할 속성
    list_display = (
        'id',
        'name',
        'price',
        'stock',
        'seller',
        'created_at',
    )
    # 검색을 위한 속성
    search_fields = (
        'name',
    )
    

# Review(후기)
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    # 목록에 표시할 속성
    list_display = (
        'id',
        'writer',
        'product',
        'rating',
    )
    # 검색을 위한 속성
    search_fields = (
        'writer',
    )
