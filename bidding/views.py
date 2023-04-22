from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from seller_dashboard.models import Car
from rest_framework.views import APIView
from rest_framework import status
from knox.auth import TokenAuthentication
from bidding.serializers import AuctionSerializer, OfferSerializer, BidOfferSerializer
from seller_dashboard.serializers import CarSerializer
from seller_dashboard.models import BidOffer
from bidding.models import Auction
from django.shortcuts import get_object_or_404
from bidding.permissions import IsDealer
import asyncio
from bidding.sending_notification import bid_message

class AuctionView(APIView):
    serializer_class = CarSerializer
    model = Auction
    serializer_class = AuctionSerializer

    def get(self, request):
        if self.model.objects.filter(ended = False):
            auction = Auction.objects.get(ended = False)
            serializer = self.serializer_class(auction, context = {"request": request})
            return Response(serializer.data)
        else:
            return Response({"message": "no auctions available"})
        
class AllCars(APIView):
    serializer_class = CarSerializer

    def get(self, request):
        cars = Car.objects.filter(draft = False, auctioned = False)
        serializer = self.serializer_class(cars, many = True)
        return Response(serializer.data)

class CarDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes  = [IsAuthenticated]
    serializer_class = CarSerializer
    model = Car

    def get(self, request,car_id):
        car = get_object_or_404(self.model, id = car_id)
        serializer = self.serializer_class[1](car)
        return Response(serializer.data)
       
class BidOfferView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsDealer]
    model = Car
    serializer_class = OfferSerializer

    def post(self, request, car_id):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        offer = serializer.data["offer"]
        car = get_object_or_404(self.model, id = car_id)
        bid_offer = BidOffer.objects.create(dealer = request.user, offer = offer)
        car.offers.add(bid_offer)

        asyncio.run(bid_message(bid_offer.offer, car.id))


        serializer = BidOfferSerializer(bid_offer)
        return Response(serializer.data)
