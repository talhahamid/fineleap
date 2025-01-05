from .models import Enquiry
from django.http import HttpResponse, JsonResponse
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.contrib import messages

def homepage(request):
    return render(request, 'home.html')


def enquiry_form(request):
    print('hi')
    if request.method == 'POST':
        print('hiii')
        name = request.POST.get('name', 'Anonymous')
        email = request.POST.get('email', 'No email provided')
        message = request.POST.get('message', 'No message provided')
        subject = request.POST.get('subject', 'No subject provided')
        print('hiiiyyy',name,email,message,subject)

        # Construct the email
        email_subject = "New Contact Form Submission"
        email_body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        recipient_list = [
            'talhahamid.syed@gmail.com',
            'hr@fineleap.co.in',
            'info@fineleap.co.in',
        ]
        print('heyyyy',recipient_list)

        try:
            email = EmailMessage(email_subject, email_body, to=recipient_list)
            email.send()
            print('yes',email)
            messages.success(request, 'Your message was sent successfully!')
            print(messages,'Your message was sent successfully!')
            return JsonResponse({"success": True})
        except Exception as e:
            print(f"Error sending email: {e}")
            messages.error(request, 'An error occurred while sending your message.')
            return JsonResponse({"success": False, "error": str(e)})
    return JsonResponse({"success": False, "error": "Invalid request method."})
