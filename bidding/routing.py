from django.urls import path
from bidding.consumers import NotificationConsumer, CarOfferConsumer, PersonalNotificationsConsumer
from accounts.middlewares import TokenAuthMiddleware

websocket_urlpatterns = [
    path('general_notifications/', NotificationConsumer.as_asgi() ),
    path('offers/<str:car_id>/', CarOfferConsumer.as_asgi()),
    path("notifications/<str:user_id>/", TokenAuthMiddleware(PersonalNotificationsConsumer.as_asgi())),

]