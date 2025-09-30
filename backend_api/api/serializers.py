from rest_framework import serializers
from core.models import Bike
from events.models import Events


class BikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = "__all__"

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model= Events
        fields = '__all__'