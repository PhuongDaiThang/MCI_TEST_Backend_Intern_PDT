from rest_framework import serializers
from .models import TaskBoard

class TaskBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskBoard
        fields = '__all__'
