from celery import shared_task
from bidding.models import Auction
from seller_dashboard.models import Car
from bidding.models import BidSetting
from django.utils import timezone
import datetime
  
bid_setting = BidSetting.objects.all().first()

@shared_task
def bids():
    
    if timezone.now().time() >= bid_setting.start_time or timezone.now().time() <= bid_setting.end_time:
        time_of_advert = timezone.now() - datetime.timedelta(hours=72)
        start_time = timezone.now() - datetime.timedelta(hours=2)

        if Auction.objects.exists() == True:
            last_auction = Auction.objects.all().last()

            if last_auction.start <= start_time and last_auction.ended == False and Car.objects.filter(time_of_advert__lte=time_of_advert, draft=False, auctioned = False).exists():

                last_auction.ended =True
                last_auction.save()

                cars = Car.objects.filter(time_of_advert__lte=time_of_advert, draft=False, auctioned = False)[:200]
                auction = Auction.objects.create(start = timezone.now())
                auction.cars.add(*cars)

                for car in auction.cars.all():
                    car.auctioned = True
                    car.save()

        elif Auction.objects.exists() == False and Car.objects.filter(time_of_advert__lte=time_of_advert, draft=False).exists() == True:
            cars = Car.objects.filter(time_of_advert__lte=time_of_advert, draft=False)[:200]
            auction = Auction.objects.create(start = timezone.now())
            auction.cars.add(*cars)

            for car in auction.cars.all():
                car.auctioned = True
                car.save()


    
        