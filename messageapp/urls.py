from django.contrib import admin
from django.urls import path, include
from .views import SendMessageView, InboxView, ReadMessageView


urlpatterns = [
    path('send_message/<int:receiver_id>/', SendMessageView.as_view(), name='send_message'),
    path('inbox/', InboxView.as_view(), name='inbox'),
    path('read_message/<int:pk>/', ReadMessageView.as_view(), name='read_message'),
       
        
]