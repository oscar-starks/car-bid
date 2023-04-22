from django.contrib import admin
from seller_dashboard.models import Car, CarImage,BidOffer

admin.site.register([Car, CarImage,BidOffer])