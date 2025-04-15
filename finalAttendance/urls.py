from django.contrib import admin
from django.urls import path, include
from .views import AttendanceListView
urlpatterns = [
   path('attendance/', AttendanceListView.as_view(), name='attendance-list'),
       
]