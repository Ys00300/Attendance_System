from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import View

from .models import CustomUser

# Create your views here.

user = get_user_model()

class CreateRegisterView(CreateView):
    model = CustomUser
    form_class = RegistrationForm
    template_name = "register.html"
    success_url = reverse_lazy("login")

    
    def form_valid(self, form):
        user = form.save()  
        login(self.request, user)  
        return super().form_valid(form)
   

class CustomLoginView(LoginView):
    template_name = 'login.html'  # Use a custom template if needed

    def get_context_data(self, **kwargs):
        # Add custom context variables to the login page template
        context = super().get_context_data(**kwargs)
        
        context['custom_message'] = 'Please login to continue.'
        return context
    
    
    def get_success_url(self):
        # Redirect users after a successful login
        user = self.request.user  # Get the logged-in user

        if user.user_type == 'teacher':
            return reverse_lazy('teacherHome')  # Redirect to the teacher's dashboard
        else:
            return reverse_lazy('home')  # Redirect to the default home page
    
    
class CustomLogoutView(LogoutView) :
      def get_next_page(self):
        next_page = self.request.GET.get('next')      
        if not next_page:
            next_page = '/login/' 
        
        return next_page
    

#login required (if user want to access home page without login or register)
class HomeView(LoginRequiredMixin,TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_name'] = self.request.user.username
        return context
    
    
#login required (if user want to access home page without login or register)
class TeacherHomeView(LoginRequiredMixin,TemplateView):
    template_name = 'teacherHome.html'
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['user_name'] = self.request.user.username
    #     return context