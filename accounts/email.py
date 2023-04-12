from accounts.models import User, AccountToken
from django.core.mail import EmailMessage
from accounts.threads import EmailThread

class Util:
    @staticmethod
    def send_recovery(user:User):
        token, created = AccountToken.objects.get_or_create(user=user, purpose = "recovery")
        subject = "Recover your account"
        
        user_name = user.first_name.capitalize() + " " + user.last_name.capitalize()
        message = f"Dear {user_name}, \n Here is your one time recovery token: {token.token}"
        email_message = EmailMessage(subject=subject, body=message, to=[user.email])
        EmailThread(email_message).start()

    def account_created(user:User):
        subject = "Signup Successful"

        user_name = user.first_name.capitalize() + " " + user.last_name.capitalize()
        message = f"Dear {user_name}, \n Your account has successfully been created and is awaiting review by the admins"
        email_message = EmailMessage(subject=subject, body=message, to=[user.email])
        EmailThread(email_message).start()

    def seller_approved(user:User):
        subject = "Seller Account Approved"

        user_name = user.first_name.capitalize() + " " + user.last_name.capitalize()
        message = f"Dear {user_name}, \n Your account has successfully been approved by the admins and you can now auction your cars on the platform"
        email_message = EmailMessage(subject=subject, body=message, to=[user.email])
        EmailThread(email_message).start()

