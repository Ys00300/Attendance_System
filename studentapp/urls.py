from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
        
        path('create/',views.CreateStudentView.as_view(),name='create_student' ),
        path('update/<int:pk>/', views.StudentUpdateView.as_view(), name='update_student'),
        path('details/<int:pk>/',views.StudentDetailview.as_view(),name='detail_student'),

        
]