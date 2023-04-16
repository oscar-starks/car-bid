from django.urls import path
from bidding.views import AuctionView

urlpatterns = [
    path('all/', AuctionView.as_view()),
]
