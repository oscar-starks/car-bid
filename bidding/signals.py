from django.dispatch import receiver
from django.db.models.signals import m2m_changed
from seller_dashboard.models import BidOffer, Car
from bidding.sending_notification import bid_message
import asyncio    
        
@receiver(m2m_changed, sender=Car.offers.through)
def offer_signal(sender, instance, action, pk_set, **kwargs):
    if action == 'post_add':
        last_offer = instance.offers.last()
        asyncio.run(bid_message(int(last_offer.offer), str(instance.id), str(last_offer.id)))

