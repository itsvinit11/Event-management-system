from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    categories = models.ManyToManyField('Category')
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        app_label = 'events'

class Category(models.Model):
    name = models.CharField(max_length=255)
    # Add any additional fields as per your requirements

class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

class Venue(models.Model):
    name = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    amenities = models.TextField()
    availability = models.BooleanField(default=True)
    events = models.ManyToManyField(Event, related_name='venues')

# Additional fields can be added to the User model as per your requirements
