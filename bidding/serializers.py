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
        exclude = ['dealer']