from django.urls import path
from bidding.consumers import NotificationConsumer, CarOfferConsumer
from accounts.middlewares import TokenAuthMiddleware

websocket_urlpatterns = [
    path('general_notifications/', NotificationConsumer.as_asgi() ),
    path('offers/<str:car_id>/', TokenAuthMiddleware(CarOfferConsumer.as_asgi()))

]