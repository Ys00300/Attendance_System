from django.contrib import admin
from django.urls import path
from .views import CreateRegisterView, CustomLoginView, CustomLogoutView, HomeView,TeacherHomeView
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
            
            path('', CreateRegisterView.as_view(), name='register'),  # base URL
            path('register/', CreateRegisterView.as_view()),  
            path('home', HomeView.as_view(), name='home'),
            path('login/', CustomLoginView.as_view(), name='login'),
            path('logout/', CustomLogoutView.as_view(), name='logout'),
            path('teacherHome/',TeacherHomeView.as_view(),name='teacherHome'),
            
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
