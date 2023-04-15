from django.contrib import admin
from seller_dashboard.models import Car, CarImage

admin.site.register([Car, CarImage])