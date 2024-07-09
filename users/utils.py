from django.core.mail import EmailMessage, get_connection
import os

class Util:
    @staticmethod
    def send_email(data):
        try:
            email = EmailMessage(
                subject=data['subject'],
                body=data['body'],
                from_email=os.environ.get('EMAIL_FROM'),
                to=[data['to_email']],
                connection=get_connection(
                    username=os.environ.get('EMAIL_HOST_USER'),
                    password=os.environ.get('EMAIL_HOST_PASSWORD'),
                    fail_silently=False
                )
            )
            email.send()
            return True
        except Exception as e:
            print(f"Failed to send email: {e}")
            return False
