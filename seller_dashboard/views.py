from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from seller_dashboard.serializers import CarSerializer, CarStatusUpdateSerializer,AddCarSerializer, UpdateCarSerializer,CarImageSerializer
from seller_dashboard.models import Car
from rest_framework.views import APIView
from rest_framework import status
from knox.auth import TokenAuthentication
from seller_dashboard.permissions import IsSeller
from django.utils import timezone

class MyCars(APIView):
    permission_classes = [IsSeller]
    authentication_classes = [TokenAuthentication]
    serializer_class = CarSerializer
    model = Car

    def get(self, request):
        cars = self.model.objects.filter(owner = request.user)
        serializer = self.serializer_class(cars, many=True)
        return Response(serializer.data)

class CarDetailView(APIView):
    permission_classes = [IsSeller]
    authentication_classes = [TokenAuthentication]
    serializer_class = [UpdateCarSerializer, CarSerializer]
    model = Car

    def get(self, request,car_id):
        try:
            car = self.model.objects.get(id=car_id, owner = request.user)
            serializer = self.serializer_class[1](car)
            return Response(serializer.data)
        except self.model.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request, car_id):
        try:
            car = self.model.objects.get(id=car_id, owner = request.user)
            serializer = self.serializer_class[0](data = request.data)
            serializer.is_valid(raise_exception=True)
            car.__dict__.update(serializer.data)
            car.save()
            serializer = self.serializer_class[1](car)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request,car_id):
        serializer_class = CarStatusUpdateSerializer
        try:
            car = self.model.objects.get(id=car_id, owner = request.user)
            serializer = serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            car.__dict__.update(serializer.data)
            car.save()
            serializer = self.serializer_class[1](car)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, car_id):
        try:
            self.model.objects.get(id=car_id, owner = request.user, draft  = True).delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)   

class AddCar(APIView):
    permission_classes = [IsSeller]
    authentication_classes = [TokenAuthentication]
    serializer_class = [AddCarSerializer, CarSerializer]
    model = Car

    def post(self, request):
        serializer = self.serializer_class[0](data = request.data)
        serializer.is_valid(raise_exception=True)
        car = self.model.objects.create(**serializer.data|{"owner": request.user})

        serializer = self.serializer_class[1](car)
        return Response(serializer.data)

class AddImage(APIView):
    permission_classes = [IsSeller]
    authentication_classes = [TokenAuthentication]
    serializer_class = [CarImageSerializer, CarSerializer]
    model = Car

    def post(self, request, car_id):
        # try:
            car = self.model.objects.get(id=car_id, owner = request.user)
            serializer = self.serializer_class[0](data = request.data)
            serializer.is_valid(raise_exception=True)
            print(serializer.data)
            car_image = serializer.create(validated_data = serializer.data)
            car.images.add(car_image)
            serializer = self.serializer_class[1](car)
            return Response(serializer.data)
        # except:
        #     return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, car_id):
        try:
            image_id = request.data["image_id"]
            car = self.model.objects.get(id=car_id, owner = request.user)
            car.images.delete(id = image_id)
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class Advertise(APIView):
    permission_classes = [IsSeller]
    authentication_classes = [TokenAuthentication]
    serializer_class =  CarSerializer
    model = Car

    def get(self, request, car_id):
        try:
            car = self.model.objects.get(id=car_id, owner = request.user, draft = True)
            if car.images.count() < 1:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
            car.draft = False
            car.time_of_advert = timezone.now()
            car.save()
            return Response(status=status.HTTP_200_OK)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

