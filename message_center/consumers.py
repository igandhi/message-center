from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Room, Message
import json

class MessageConsumer(WebsocketConsumer):
    def connect(self):
        # get room name from scope
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        # add room to db
        Room.objects.create(room_name=self.room_name)
        # create group for room so that all connections to the room
        # can receive updates
        self.room_group_name = 'message_%s' % self.room_name
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        # accept connection
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        # get message text from input json
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # add message to database with proper room foreign key
        roomObj = Room.objects.filter(room_name=self.room_name)[0]
        Message.objects.create(room=roomObj, message_text=message)
        # send new message to all connections in group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def chat_message(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'message': message
        }))
