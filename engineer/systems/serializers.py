from rest_framework import serializers
from .models import Equipment


class EquipmentSerializer(serializers.ModelSerializer):
    """Класс для создания сериализатора в формате JSON"""

    class Meta:
        model = Equipment
        fields = '__all__'