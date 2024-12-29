from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date = models.DateTimeField()
    

class Attendee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    events = models.ManyToManyField(Event, related_name='attendees')

class Task(models.Model):
    name = models.CharField(max_length=255)
    deadline = models.DateField()
    status = models.CharField(max_length=50, choices=(('Pending', 'Pending'), ('Completed', 'Completed')))
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tasks')
    attendee = models.ForeignKey(Attendee, on_delete=models.SET_NULL, null=True, related_name='tasks')

