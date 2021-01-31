from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.core import mail

# from email.MIMEMultipart import MIMEMultipart
# from email.MIMEText import MIMEText


def mail_view(request):
    try:
        send_mail('Subject here', 'Here is the message.',
                  'from', ['to'], fail_silently=False,)
        return HttpResponse('mail as been sent')
    except:
        return HttpResponse('mail sending has been failed')
