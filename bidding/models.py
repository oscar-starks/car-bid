from django.db import models
from seller_dashboard.models import Car, BidOffer
from accounts.models import User
from django.utils import timezone
import datetime

class Auction(models.Model):
    start = models.DateTimeField(default=timezone.now)
    cars = models.ManyToManyField(Car, blank= True)
    ended = models.BooleanField(default=False)

    class Meta:
        ordering = ["start"]

class BidSetting(models.Model):
    start_time = models.TimeField(default = datetime.time(hour=9,minute=0))
    end_time = models.TimeField(default = datetime.time(hour = 16, minute = 0))

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(default = timezone.now)
    message = models.CharField(max_length = 1000, blank=True, null=True)

    class Meta:
        ordering = ["-date"]

class BidNotification(Notification):
    offer = models.ForeignKey(BidOffer, on_delete=models.CASCADE, blank=True, null=True)

    