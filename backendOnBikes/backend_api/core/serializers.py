from rest_framework import serializers
from .models import Bike, Event, BikeImage
from django.contrib.auth.models import User

class BikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = "__all__"
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

class BikeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BikeImage
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]