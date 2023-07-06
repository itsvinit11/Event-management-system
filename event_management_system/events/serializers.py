from django.utils import timezone
from rest_framework import serializers
from .models import Event, Category, Registration, Venue

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)

    def validate_date(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("Event date should be in the future.")
        return value

    def validate(self, data):
        # Perform additional validation logic based on the complete data object
        # For example, check if capacity is greater than zero, or perform custom validations
        return data
    class Meta:
        model = Event
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'

class VenueSerializer(serializers.ModelSerializer):
    events = EventSerializer(many=True)

    class Meta:
        model = Venue
        fields = '__all__'
