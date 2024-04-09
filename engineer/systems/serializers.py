from rest_framework import serializers
from .models import Equipment, Tasks


class TasksSerializer(serializers.ModelSerializer):
    """Класс для создания сериализатора Tasks"""
    class Meta:
        model = Tasks
        fields = '__all__'

class EquipmentsModel:
    def __init__(self, tasks, datetime):
        self.tasks = tasks
        self.datetime = datetime

class TasksSerializer(serializers.Serializer):
    tasks = serializers.CharField(max_length=255)
    datetime = serializers.DateTimeField()


