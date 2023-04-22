from django.urls import path
from bidding.views import AuctionView, CarDetailView, AllCars, BidOfferView

urlpatterns = [
    path("all_cars/", AllCars.as_view()),
    path('auction/', AuctionView.as_view()),
    path('car/', CarDetailView.as_view),

    path("make_offer/<str:car_id>/",BidOfferView.as_view()),
]
