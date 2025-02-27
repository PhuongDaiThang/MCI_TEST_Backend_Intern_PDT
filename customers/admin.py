# customers/admin.py
from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone')  # Hiển thị các trường chính
    search_fields = ('name', 'email')                 # Cho phép tìm kiếm theo tên và email
    list_filter = ('name',)                           # Cho phép lọc theo tên (hoặc các trường khác nếu cần)
