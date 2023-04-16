from django.db import models
from seller_dashboard.models import Car

class Auction(models.Model):
    start_time = models.DateTimeField(auto_now_add=True)
    cars = models.ManyToManyField(Car, blank= True)

    class Meta:
        ordering = ["start_time"]
