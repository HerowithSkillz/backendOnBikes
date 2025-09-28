from django.db import models
from django.contrib.auth.models import User


class Bike(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bikes')
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    year = models.IntegerField()
    image = models.ImageField(upload_to='bikes/', blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.name} ({self.year})"

class Event(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hosted_events')
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    date = models.DateTimeField()
    description = models.TextField()
    participants = models.ManyToManyField(User, related_name='events_participating', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class BikeImage(models.Model):
    bike = models.ForeignKey('Bike', on_delete=models.CASCADE, related_name='additional_images')
    image = models.ImageField(upload_to='bikes/')
    caption = models.CharField(max_length=200, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.bike.name}"