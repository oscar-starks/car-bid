from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from seller_dashboard.serializers import CarSerializer, CarUpdateSerializer,AddCarSerializer
from seller_dashboard.models import Car
from rest_framework.views import APIView
from rest_framework import status
from knox.auth import TokenAuthentication

class MyCars(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = CarSerializer
    model = Car

    def get(self, request):
        cars = self.model.objects.filter(owner = request.user)
        serializer = self.serializer_class(cars, many=True)
        return Response(serializer.data)

class CarDetailView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = CarSerializer
    model = Car

    def get(self, request,car_id):
        try:
            car = self.model.objects.get(id=car_id)
            serializer = self.serializer_class(car)
            return Response(serializer.data)
        except self.model.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request,car_id):
        serializer_class = CarUpdateSerializer
        try:
            car = self.model.objects.get(id=car_id)
            serializer = serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            car.__dict__.update(serializer.data)
            car.save()
        except self.model.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class AddCar(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = AddCarSerializer
    model = Car

    def post(self, request):
        

