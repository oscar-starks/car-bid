from accounts.models import User
from django.core.mail import EmailMessage
from accounts.threads import EmailThread
from django.utils.translation import gettext_lazy as _

class Util:
    @staticmethod
    def send_recovery(user:User, password:str):
        subject = _("Recover your account")
        
        user_name = user.first_name.capitalize() + " " + user.last_name.capitalize()
        message = _(f"Dear {user_name}, \nYou have successfully changed password with CartoBid, your temporary password is {password}. You have to change this temporary password after you login successfully. \nNote: This is a system generated mail; please do not reply to this e-mail Id.")
        email_message = EmailMessage(subject=subject, body=message, to=[user.email])
        EmailThread(email_message).start()

    def account_created(user:User):
        subject = _("Signup Successful")

        user_name = user.first_name.capitalize() + " " + user.last_name.capitalize()
        message = _(f"Dear {user_name}, \n Your account has successfully been created and is awaiting review by the admins")
        email_message = EmailMessage(subject=subject, body=message, to=[user.email])
        EmailThread(email_message).start()

    def seller_approved(user:User):
        subject = _("Seller Account Approved")

        user_name = user.first_name.capitalize() + " " + user.last_name.capitalize()
        message = _(f"Dear {user_name}, \n Your account has successfully been approved by the admins and you can now auction your cars on the platform")
        email_message = EmailMessage(subject=subject, body=message, to=[user.email])
        EmailThread(email_message).start()

    def send_password(user:User, password:str):
        subject = _("Login Credential")

        user_name = user.first_name.capitalize() + " " + user.last_name.capitalize()

        message = _(f"Dear {user_name}, \n You have successfully registered with CartoBid. Your temporary password is : {password}. You have to change this temporary password after you login successfully.\n Note: This is system generated mail; please do not reply to this e-mail Id.")

        email_message = EmailMessage(subject=subject, body=message, to=[user.email])
        EmailThread(email_message).start()



