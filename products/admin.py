# products/admin.py
from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    search_fields = ('name',)
    list_filter = ('price',)  # Lọc theo giá (có thể thêm các mức giá khác nếu cần)
