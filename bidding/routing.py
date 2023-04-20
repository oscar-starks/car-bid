from django.urls import re_path
from bidding.consumers import NotificationConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', NotificationConsumer.as_asgi() )
    # re_path(r'ws/socket-server/', consumers.ChatConsumer.as_asgi())
]