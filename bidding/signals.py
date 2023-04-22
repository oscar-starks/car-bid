from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from seller_dashboard.models import BidOffer, Car
from sending_notification import bid_message
import asyncio

@receiver(post_save, sender=Car)
def offer_signal(sender, instance, **kwargs):
    asyncio.run(bid_message(instance.offer, ))
        
        
@receiver(pre_save, sender=Car)
def offer_signal(sender,instance, **kwargs):
    car = instance
    try:
        initial_car_state = Car.objects.get(id = car.id)

        if initial_car_state.offers.all().count() < car.offers.all().count():
            q1 = initial_car_state.offers.all().count()
            q2 = car.offers.all().count()

            new_offers = set(q2).difference(set(q1))

            for offer in new_offers:
                asyncio.run(bid_message(offer.offer, car.id))

    except:
        pass
