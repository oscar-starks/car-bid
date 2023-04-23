from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
import os
from accounts.models import User
from car_bid.settings import MEDIA_ROOT
from accounts.email import Util

@receiver(pre_delete, sender=User)
def remove_identification(sender, instance,*args, **kwargs):
    if instance.identification != None:
        try:
            id_url = instance.identification.name
            final_url = MEDIA_ROOT + '/' + id_url
            os.remove(final_url)
        except:
            pass

# @receiver(post_save, sender=User)
# def send_activation_email(sender,instance, created,**kwargs):
#     if created == True:
#         if instance.seller == True:
#             Util.account_created(instance)

@receiver(pre_save, sender=User)
def send_confirmation_email(sender,instance, **kwargs):
    user = instance
    try:
        pre_user = User.objects.get(id = user.id)

        if pre_user.approved_seller != user.approved_seller and user.approved_seller == True:
            Util.seller_approved(user = user)
    except:
        pass



