from rest_framework import serializers
from accounts.models import User, GENDER_CHOICES

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        if User.objects.filter(email = attrs["email"]).exists() == False:
            raise serializers.ValidationError("A user with that email does not exist")
        
        return attrs
    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password"]
     
class UserCreationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    gender = serializers.ChoiceField(choices = GENDER_CHOICES)
    address = serializers.CharField()
    vat_no = serializers.CharField()
    hrb_no = serializers.CharField()
    company_reg_no = serializers.CharField()
    tax_id_number = serializers.CharField()
    identification = serializers.FileField()
    dealer = serializers.BooleanField(default=True)
    seller = serializers.BooleanField(default=False)


    def validate(self, attrs):
        if User.objects.filter(email = attrs["email"]).exists():
            raise serializers.ValidationError("A user with that email already exists!")
        
        return attrs
    
class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, attrs):
        email = attrs["email"]
        if User.objects.filter(email = email).exists() == False:
            raise serializers.ValidationError(f"User with email {email} does not exist")
        return attrs

