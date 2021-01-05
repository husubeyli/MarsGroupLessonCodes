import time
from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from stories.models import Subscriber, Recipe


@shared_task
def dump_database():
    print('database dump olunmaga basladi')
    time.sleep(60)
    print('database dump olundu')


@shared_task
def send_mail_to_subscribers():
    subscriber_emails = Subscriber.objects.values_list('email', flat=True)
    recipes = Recipe.objects.all()

    context = {
        'site_address': settings.SITE_ADDRESS,
        'recipes': recipes
    }

    html_message = render_to_string('email-subscribers.html', context)
    subject = 'News About our site'

    email = EmailMessage(subject=subject, body=html_message, from_email=settings.EMAIL_HOST_USER, to=subscriber_emails)
    email.content_subtype = 'html'
    email.send()


# background tasks
# concurrency
# periodic task
