from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="CRM API",
      default_version='v1',
      description="Tài liệu API cho hệ thống CRM",
      terms_of_service="https://www.example.com/terms/",
      contact=openapi.Contact(email="contact@example.com"),
      license=openapi.License(name="BSD License"),
   ),
    public=True,
    permission_classes=(permissions.AllowAny,), 
)

admin.site.site_header = "Quản trị CRM"
admin.site.site_title = "Trang quản trị CRM"
admin.site.index_title = "Chào mừng đến với trang quản trị CRM"

urlpatterns = [
    # Đăng nhập, token JWT
    path('api/auth/', include('accounts.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Admin
    path('admin/', admin.site.urls),

    # Các app trong dự án
    path('api/customers/', include('customers.urls')),
    path('api/products/', include('products.urls')),
    path('api/employees/', include('employees.urls')),
    path('api/taskboards/', include('taskboards.urls')),

    # Swagger & Redoc
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
]
