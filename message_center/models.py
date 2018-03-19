from django.db import models
from django.utils import timezone

class Room(models.Model):
    room_name = models.TextField()

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    message_text = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)
