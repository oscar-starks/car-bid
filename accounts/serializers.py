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
    avatar = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        exclude = ["password"]

    def get_avatar(self, obj):
        try:
            request = self.context.get("request")
            return request.build_absolute_uri(obj.avatar.url)
        except:
            return None
        
class UserCreationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    gender = serializers.ChoiceField(choices = GENDER_CHOICES)
    password = serializers.CharField()
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
        
        elif len(attrs["password"]) < 8:
            raise serializers.ValidationError("password is too short!")

        return attrs