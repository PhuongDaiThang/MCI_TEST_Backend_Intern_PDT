from rest_framework import viewsets, filters
from .models import TaskBoard
from .serializers import TaskBoardSerializer

class TaskBoardViewSet(viewsets.ModelViewSet):
    queryset = TaskBoard.objects.all()
    serializer_class = TaskBoardSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    # Cho phép tìm kiếm theo trạng thái và nhân sự (giả sử trường nhân sự là assigned_to__id hoặc assigned_to__first_name)
    search_fields = ['status', 'assigned_to__first_name', 'assigned_to__last_name']
