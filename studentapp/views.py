from django.shortcuts import render, redirect
from AttendanceSystem.models import CustomUser
from django.views.generic.list import ListView 
from django.views.generic.edit import CreateView ,UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import StudentForms
from .forms import CustomUserForm
from .models import Student, CustomUser
# Create your views here.

class CreateStudentView(LoginRequiredMixin,CreateView):
    model = CustomUser
    fields = ['gender','section','branch','en_Number']
    template_name = 'studentapp/create.html'
    success_url = reverse_lazy('update_student')

class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserForm  # Use a form if you have one, otherwise keep `fields`
    template_name = 'update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object

        # Ensure a Student object exists for this user
        student, _ = Student.objects.get_or_create(user=user)

        if self.request.method == 'POST':
            context['student_form'] = StudentForms(self.request.POST, self.request.FILES, instance=student)
        else:
            context['student_form'] = StudentForms(instance=student)

        return context

    def form_valid(self, form):
        context = self.get_context_data()
        student_form = context['student_form']

        if student_form.is_valid():
            self.object = form.save()  # Save the CustomUser
            student = student_form.save(commit=False)
            student.user = self.object
            student.save()
            return redirect(self.get_success_url())

        return self.form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('detail_student', kwargs={'pk': self.object.pk})
class StudentDetailview(LoginRequiredMixin,DetailView):
    
    model = CustomUser
    template_name = 'detail.html'
    
  
