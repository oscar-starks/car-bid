from rest_framework import serializers
from seller_dashboard.serializers import CarSerializer
from bidding.models import Auction

class AuctionSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many = True, read_only = True)
    class Meta:
        model = Auction
        fields  = "__all__"
