from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
        
        path('create/',views.CreateTeacherView.as_view(),name='create_teacher' ),
        path('update/<int:pk>/', views.teacherUpdateview.as_view(), name='update_teacher'),
        path('details/<int:pk>/',views.teacherDetailview.as_view(),name='detail_teacher'),

        
        
]