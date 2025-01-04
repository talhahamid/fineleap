from django.contrib import admin
from .models import Enquiry

admin.site.site_header = 'Fine-Leap Systems'
admin.site.site_title = 'Fine-Leap Systems'
admin.site.register(Enquiry)
