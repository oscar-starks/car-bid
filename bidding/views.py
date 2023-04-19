from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from seller_dashboard.models import Car
from rest_framework.views import APIView
from rest_framework import status
from knox.auth import TokenAuthentication
from bidding.serializers import AuctionSerializer
from seller_dashboard.serializers import CarSerializer
from bidding.models import Auction
from django.utils import timezone
import datetime

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

        
        # start_time = timezone.now() - datetime.timedelta(hours=2)

        # if (Auction.objects.filter(start_time__gte = start_time).exists() == True
        #     and self.model.objects.filter(time_of_advert__lte=time_of_advert, draft=False).exists() == False):






        # cars = self.model.objects.filter(time_of_advert__lte=time_of_advert).order_by('time_of_advert')[:200]
        # serializer = self.serializer_class(cars, many = True, context = {"request": request})
        # return Response(serializer.data)

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