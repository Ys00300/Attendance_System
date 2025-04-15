from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import get_user_model, login
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from finalAttendance.models import Subject
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

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
    


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_name'] = self.request.user.username

        # Show message only if profile is not updated AND message not shown before
        user = self.request.user
        if not hasattr(user, 'teacher') and not self.request.session.get('profile_warning_shown'):
            messages.warning(self.request, 'Please update your profile first.')
            self.request.session['profile_warning_shown'] = True  # Set flag to avoid showing again

        return context

    

class TeacherHomeView(LoginRequiredMixin,TemplateView):
    template_name = 'teacherhome.html' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teacher = self.request.user.teacher  
        context['subject'] = Subject.objects.filter(teachers=teacher)
        
        return context
