from .models import Enquiry
from django.http import HttpResponse, JsonResponse
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.contrib import messages

def homepage(request):
    return render(request, 'home.html')


def enquiry_form(request):
    if request.method == 'POST':
        print("Received a POST request")  # This will appear in Render logs
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        print(f"Form Data: Name={name}, Email={email}, Message={message}, Subject={subject}")

        # Construct and send email
        try:
            email = EmailMessage(
                "New Contact Form Submission",
                f"Name: {name}\nEmail: {email}\nMessage: {message}",
                to=['talhahamid.syed@gmail.com']
            )
            email.send()
            print("Email sent successfully!")
            return JsonResponse({"success": True})
        except Exception as e:
            print(f"Error sending email: {e}")
            return JsonResponse({"success": False, "error": str(e)})

    print("Invalid request method")
    return JsonResponse({"success": False, "error": "Invalid request method."})
