from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from accounts.serializers import LoginSerializer, UserCreationSerializer, UserProfileSerializer, ForgotPasswordSerializer
from accounts.custom_functions import authenticate_user
from accounts.models import User
from accounts.email import Util
from knox.auth import AuthToken, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from accounts.custom_functions import generate_random_string


class LoginView(APIView):
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
        password = generate_random_string()
        user = User.objects.create_user(**serializer.validated_data|{'password':password})
        user.save()
        Util.send_password(user = user, password = password)
        return Response({'success': True}, status=status.HTTP_200_OK)
    
class UserProfile(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = [UserProfileSerializer]
    
    def get(self, request):
        user = request.user
        serializer = self.serializer_class[0](user,many = False,context={"request": request})
        return Response(serializer.data)

class Logout(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        AuthToken.objects.filter(user = request.user).delete()
        return Response({"logout": True})
            
class ForgotPassword(APIView):
    serializer_class = ForgotPasswordSerializer
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        
        password = generate_random_string()
        user = User.objects.get(email = serializer.data["email"])
        user.set_password(password)
        user.save()

        Util.send_recovery(user=user, password=password)
        return Response(status=status.HTTP_201_CREATED)

class ChangePasswordView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        password = request.data.get("password")

        if password != None:
            if len(password) < 8:
                return Response({"message": "Password is too short"}, status=status.HTTP_400_BAD_REQUEST)
            
            user.set_password(password)
            user.save()
            return Response({"message": "Password changed"}, status=status.HTTP_200_OK)
            
        else:
            return Response({"message": "Password not provided"}, status=status.HTTP_400_BAD_REQUEST)