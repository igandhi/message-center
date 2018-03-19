from django.shortcuts import render
from django.utils.safestring import mark_safe
from .models import Room, Message
import json

def index(request):
    # show all available rooms on homepage
    rooms = Room.objects.all()
    return render(request, 'message_center/index.html', {
        'rooms': rooms
    })

def room(request, room_name):
    # get available messages for current room
    messages = Message.objects.filter(room__room_name = room_name)
    return render(request, 'message_center/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'messages': messages
    })
