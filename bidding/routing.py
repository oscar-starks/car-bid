from django.urls import path, re_path
from bidding.consumers import NotificationConsumer

websocket_urlpatterns = [
    path('general_notifications/', NotificationConsumer.as_asgi() )
    # re_path(r'(?P<user_id>\w+)/$', NotificationConsumer.as_asgi())

]