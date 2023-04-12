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
        email_message.content_subtype = "html"
        EmailThread(email_message).start()