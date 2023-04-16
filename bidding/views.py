from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from seller_dashboard.models import Car
from rest_framework.views import APIView
from rest_framework import status
from knox.auth import TokenAuthentication
from seller_dashboard.permissions import IsSeller
from seller_dashboard.serializers import CarSerializer
from django.utils import timezone
import datetime

class AuctionView(APIView):
    serializer_class = CarSerializer
    model = Car

    def get(self, request):
        time_of_advert = timezone.now() - datetime.timedelta(hours=72)
        cars = self.model.objects.filter(time_of_advert__lte=time_of_advert).order_by('time_of_advert')[:200]
        serializer = self.serializer_class(cars, many = True, context = {"request": request})
        return Response(serializer.data)

