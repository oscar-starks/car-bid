from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from accounts.serializers import LoginSerializer, UserCreationSerializer, UserProfileSerializer, ForgotPasswordSerializer, NewPasswordSerializer
from accounts.custom_functions import authenticate_user
from accounts.models import User, AccountToken
from accounts.email import Util
from knox.auth import AuthToken, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

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
            
        serializer = UserProfileSerializer(user, many = False, context ={"request":request})
        token = AuthToken.objects.create(user=user)
        return Response({"token":token[1]}|dict(serializer.data))
    
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
        
        user = User.objects.get(email = serializer.data["email"])
        Util.send_recovery(user=user)
        return Response(status=status.HTTP_201_CREATED)

class NewPasswordView(APIView):
    serializer_class = [NewPasswordSerializer,UserProfileSerializer]
    def post(self, request):
        serializer = self.serializer_class[0](data = request.data)
        serializer.is_valid(raise_exception=True)

        token = serializer.data["token"]
        token = AccountToken.objects.get(token=token, purpose = "recovery")
        user = token.user
        user.set_password(serializer.data["password"])
        user.save()
        del token

        serializer = self.serializer_class[1](user, many = False, context = {"request":request})
        token = AuthToken.objects.create(user=user)
        return Response({"token":token[1]}|dict(serializer.data))

    
    # def put(self, request):
    #     user = request.user

    #     serializer = self.serializer_class[1](data=request.data)
    #     serializer.is_valid(raise_exception=True)

    #     for data in serializer.data:
    #         setattr(user, data, request.data[data])
    #     user.save()

    #     serializer  = self.serializer_class[0](user)
    #     return Response(serializer.data)