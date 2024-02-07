from rest_framework import serializers
from .models import Equipment, Tasks


class TasksSerializer(serializers.ModelSerializer):
    """Класс для создания сериализатора в формате JSON"""

    class Meta:
        model = Tasks
        fields = '__all__'


class TasksSerializer(serializers.Serializer):
    tasks = serializers.CharField(max_length=255)
    datetime = serializers.DateTimeField()
