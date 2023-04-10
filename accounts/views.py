from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from accounts.serializers import LoginSerializer, UserCreationSerializer
from accounts.custom_functions import authenticate_user
from accounts.models import User


class APILoginView(APIView):
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        return authenticate_user(request = request, **serializer.validated_data) 
    
class CreateUser(APIView):
    serializer_class = UserCreationSerializer
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(**serializer.validated_data)
        user.is_active = False
        user.save()
        return Response(status=status.HTTP_201_CREATED)