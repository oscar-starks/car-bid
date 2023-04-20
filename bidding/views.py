from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from seller_dashboard.models import Car
from rest_framework.views import APIView
from rest_framework import status
from knox.auth import TokenAuthentication
from bidding.serializers import AuctionSerializer
from seller_dashboard.serializers import CarSerializer
from bidding.models import Auction

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
    serializer_class = CarSerializer
    model = Car

    def get(self, request,car_id):
        try:
            car = self.model.objects.get(id=car_id)
            serializer = self.serializer_class[1](car)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)