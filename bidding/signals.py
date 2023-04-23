from django.dispatch import receiver
from django.db.models.signals import m2m_changed, post_save
from seller_dashboard.models import Car
from bidding.sending_notification import bid_message, personal_notifcations
from bidding.models import Notification, BidNotification
import asyncio    
        
@receiver(m2m_changed, sender=Car.offers.through)
def offer_signal(sender, instance, action, pk_set, **kwargs):
    if action == 'post_add':
        last_offer = instance.offers.last()
        asyncio.run(bid_message(int(last_offer.offer), str(instance.id), str(last_offer.id)))
        BidNotification.objects.create(user = instance.owner, offer = last_offer)

@receiver(post_save, sender=Notification)
def notification_signal(sender, instance, created, **kwargs):
    user = instance.user
    if created:
        asyncio.run(personal_notifcations(str(user.id), "new notification"))

@receiver(post_save, sender=BidNotification)
def bid_notification_signal(sender, instance, created, **kwargs):
    user = instance.user
    if created:
        asyncio.run(personal_notifcations(str(user.id), "new bid notification"))

