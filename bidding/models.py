from django.db import models
from seller_dashboard.models import Car
from django.utils import timezone
import datetime

class Auction(models.Model):
    start_time = models.DateTimeField(auto_now_add=True)
    cars = models.ManyToManyField(Car, blank= True)

    class Meta:
        ordering = ["start_time"]

    @property
    def time_elapsed(self) -> bool:
        duration_time = timezone.now() - datetime.timedelta(hours=2)
        if self.start_time > duration_time:
            return True
        else:
            return False


