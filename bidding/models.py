from django.db import models
from seller_dashboard.models import Car
from django.utils import timezone
import datetime

class Auction(models.Model):
    start = models.DateTimeField(default=timezone.now)
    cars = models.ManyToManyField(Car, blank= True)
    ended = models.BooleanField(default=False)

    class Meta:
        ordering = ["start"]

    # @property
    # def time_elapsed(self) -> bool:
    #     duration_time = timezone.now() - datetime.timedelta(hours=2)
    #     if self.start_time > duration_time:
    #         return True
    #     else:
    #         return False

class BidSetting(models.Model):
    start_time = models.TimeField(default = datetime.time(hour=9,minute=0))
    end_time = models.TimeField(default = datetime.time(hour = 16, minute = 0))

