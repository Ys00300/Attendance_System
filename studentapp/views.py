from django.shortcuts import render
from AttendanceSystem.models import CustomUser
from django.views.generic.list import ListView 
from django.views.generic.edit import CreateView ,UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
# Create your views here.

class CreateStudentView(CreateView):
    model = CustomUser
    fields = ['gender','section','branch','en_Number']
    template_name = 'studentapp/create.html'
    success_url = reverse_lazy('update_student')


class StudentUpdateview(UpdateView):
    model = CustomUser
    fields = ['gender','section','branch','en_Number']
    template_name = 'update.html'

    def get_success_url(self):
        return reverse_lazy('detail_student', kwargs={'pk': self.object.id})

class StudentDetailview(DetailView):
    model = CustomUser
    template_name = 'detail.html'


