from django.shortcuts import render
from .models import Enquiry
from django.http import HttpResponse, JsonResponse


def homepage(request):
    return render(request, 'home.html')


def enquiry_form(request):
    if request.method == 'POST':
        #print(555)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        #Enquiry.objects.create(name=name, email=email, message=message, subject=subject)
        # Construct the email
        subject = "New Contact Form Submission"
        body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        recipient1 = 'talhahamid.syed@gmail.com'  # Replace with your HR email
        recipient2 =  'hr@fineleap.co.in' # Replace with your HR email
        recipient3 = 'info@fineleap.co.in'  # Replace with your HR email

        try:
            email = EmailMessage(subject, body, to=[recipient1,recipient2,recipient3])
            email.send()
            messages.success(request, 'Your message was sent successfully!')
        except Exception as e:
            print(f"Error: {e}")
            messages.error(request, 'An error occurred while sending your message.')

    # return HttpResponse('success')
    return JsonResponse({"success": "success"})

