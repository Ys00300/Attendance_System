from django.contrib import admin
from django.urls import path, include
from . import views
from .views import MarkAttendanceView
urlpatterns = [
        
        path('create_teacher/',views.CreateTeacherView.as_view(),name='create_teacher' ),
        path('update_teacher/<int:pk>/', views.TeacherUpdateView.as_view(), name='update_teacher'),
        path('teacher_details/<int:pk>/',views.TeacherDetailview.as_view(),name='teacher_details'),  
        path('mark-attendance/<int:pk>/', MarkAttendanceView.as_view(), name='mark_attendance'),
        
]