from django.urls import path
from bidding.views import AuctionView, CarDetailView

urlpatterns = [
    path('all/', AuctionView.as_view()),
    path('car/', CarDetailView.as_view),
]
