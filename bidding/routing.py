from django.urls import path
from bidding.consumers import NotificationConsumer, CarOfferConsumer

websocket_urlpatterns = [
    path('general_notifications/', NotificationConsumer.as_asgi() ),
    path('offers/<str:car_id>/', CarOfferConsumer.as_asgi())

]