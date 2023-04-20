from django.contrib import admin
from bidding.models import Auction, BidSetting, Notification, BidOffer

admin.site.register([Auction, BidSetting, Notification, BidOffer])