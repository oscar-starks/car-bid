from rest_framework import serializers
from seller_dashboard.serializers import CarSerializer
from seller_dashboard.models import BidOffer
from bidding.models import Auction

class AuctionSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many = True, read_only = True)
    class Meta:
        model = Auction
        fields  = "__all__"

class OfferSerializer(serializers.Serializer):
    offer = serializers.IntegerField()

class BidOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = BidOffer
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['dealer'] = instance.dealer.first_name

        return representation