from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from seller_dashboard.models import BidOffer, Car
from bidding.sending_notification import bid_message
import asyncio
      
@receiver(pre_save, sender=Car)
def offer_signal(sender,instance, **kwargs):
    asyncio.run(bid_message(5000, str(instance.id)))
