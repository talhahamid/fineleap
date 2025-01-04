#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('enquiry_form/', views.enquiry_form, name='enquiry_form'),
]









