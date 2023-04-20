from django.contrib import admin
from bidding.models import Auction, BidSetting, Notification

admin.site.register([Auction, BidSetting, Notification])