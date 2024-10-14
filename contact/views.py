from django.shortcuts import render

from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the Contact Page!</h1>")


@csrf_exempt
def contact_form(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')

        subject = f'New message from {name}'
        message_body = f'Name: {name}\nEmail: {email}\nMessage: {message}'

        send_mail(
            subject,
            message_body,
            'nahidallhv@gmail.com',  
            ['nahidallhv@gmail.com'],  
            fail_silently=False,
        )
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)
