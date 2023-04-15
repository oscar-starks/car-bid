from django.db import models
from accounts.models import User
import uuid

class CarImage(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    image = models.ImageField(upload_to = "car_image/")

class Car(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    model = models.CharField(max_length=1000)
    km = models.PositiveIntegerField()
    first_registration_date = models.DateField()
    power = models.CharField(max_length=1000)
    price = models.PositiveIntegerField()
    images = models.ManyToManyField(CarImage, blank= True)
    paid = models.BooleanField(default=False)
    sold = models.BooleanField(default=False)
    picked_up = models.BooleanField(default=False)
    draft = models.BooleanField(default=True)
    time_of_advert = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.model
