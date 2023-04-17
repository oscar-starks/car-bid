from rest_framework import serializers
from seller_dashboard.models import Car, CarImage

class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = "__all__"

    def create(self, validated_data):
        image = validated_data["image"]
        car_image = CarImage.objects.create(image = image)
        return car_image

class CarSerializer(serializers.ModelSerializer):
    images = CarImageSerializer(many = True)
    class Meta:
        model = Car
        exclude = ["owner",]


class AddCarSerializer(serializers.Serializer):
    model = serializers.CharField()
    price = serializers.IntegerField()
    km = serializers.CharField()
    first_registration_date = serializers.DateField()
    power = serializers.CharField()

class CarStatusUpdateSerializer(serializers.Serializer):
    paid = serializers.BooleanField(required=False)
    sold = serializers.BooleanField(required=False)
    picked_up = serializers.BooleanField(required=False)

    def validate(self, attrs):
        all_stat = False
        for con in ["paid", "sold", "picked_up"]:
            if con in attrs:
                all_stat = True
                break

        if all_stat == False:
            raise serializers.ValidationError('at least one field must be provided')
        return attrs

class UpdateCarSerializer(serializers.Serializer):
    model = serializers.CharField(required = False)
    km = serializers.IntegerField(required = False)
    first_registration_date = serializers.DateField(required = False)
    power = serializers.CharField(required = False)

    def validate(self, attrs):
        all_stat = False
        for con in ["model", "km", "first_registration_date", "power"]:
            if con in attrs:
                all_stat = True
                break

        if all_stat == False:
            raise serializers.ValidationError('at least one field must be provided')
        return attrs