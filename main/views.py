from django.shortcuts import render

from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def email(request):
    
    send_mail(
        'Hello',
        'Lets go',
        'settings.EMAIL_HOST_USER',
        ['jovoooi2008@gmail'],
        fail_silently=False
    )

    return render(request, 'email.html')