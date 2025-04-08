from django.contrib import admin
from django.urls import path, include
from .views import SendEmailView
urlpatterns = [
     path('send-mail/', SendEmailView.as_view(), name='send_mail'),
       
        
]