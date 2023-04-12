from django.db import models
import uuid

class CarImage(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    image = models.ImageField(upload_to = "car_image/")

class Car(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    model = models.CharField(max_length=1000)
    km = models.PositiveIntegerField(max_length=1000)
    first_registration_date = models.DateField()
    power = models.CharField(max_length=1000)
    images = models.ManyToManyField(CarImage)

    def __str__(self):
        return self.model
