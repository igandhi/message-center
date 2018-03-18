from django.conf.urls import url
from . import consumers

websocket_urlpatterns = [
    url(r'^ws/message_center/(?P<room_name>[^/]+)/$', consumers.MessageConsumer),
]
