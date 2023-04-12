from knox.auth import AuthToken
from django.contrib.auth import authenticate
from accounts.serializers import UserProfileSerializer
from rest_framework.response import Response
import secrets, string

def authenticate_user(request, email, password):
    user = authenticate(request, email = email, password = password)
            
    if user is None:
        return Response({"error":"Invalid details!"})
    
    serializer = UserProfileSerializer(user, many = False, context = {"request": request})
    
    token = AuthToken.objects.create(user=user)
    return Response({"token":token[1]}|dict(serializer.data))

