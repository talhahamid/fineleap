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
        Enquiry.objects.create(name=name, email=email, message=message, subject=subject)
    # return HttpResponse('success')
    return JsonResponse({"success": "success"})

