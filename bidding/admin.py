from django.contrib import admin
from bidding.models import Auction, BidSetting, Notification, BidNotification

admin.site.register([Auction, BidSetting, Notification, BidNotification])