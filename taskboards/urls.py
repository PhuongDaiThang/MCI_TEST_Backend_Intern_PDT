from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskBoardViewSet

router = DefaultRouter()
router.register(r'', TaskBoardViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
