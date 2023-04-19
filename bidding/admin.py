from django.contrib import admin
from bidding.models import Auction, BidSetting

admin.site.register([Auction, BidSetting])