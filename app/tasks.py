from __future__ import absolute_import, unicode_literals

from celery import shared_task
from celery.utils.log import get_task_logger

from django.core.mail import send_mail, BadHeaderError

from app.models import User
from app.serializers import DataSerializer

from django.conf import settings

from main.celery import app

logger = get_task_logger(__name__)


@shared_task(bind=True)
def send_email(self):
    for user in User.objects.all():
        try:
            send_mail(
                subject="Test email subject!",
                message='Test email message',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
                fail_silently=False,
            )
            status = 'Email sent'
        except BadHeaderError:
            logger.info('Bad header error')
            status = 'Email not sent'
        except Exception as e:
            logger.error(e)
            status = 'Email not sent'
        save_email_status(user, status)


def save_email_status(user, status):
    data_to_save = {
        'name': user.name,
        'email': user.email,
        'status': status
    }
    serializer = DataSerializer(data=data_to_save)
    serializer.is_valid(raise_exception=True)
    serializer.save()
