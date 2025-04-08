from django.shortcuts import render
from .models import Teacher
from django.views.generic.edit import CreateView ,UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
# Create your views here.

class CreateTeacherView(CreateView):
    model = Teacher
    fields = ['branch','subject','image']
    template_name = 'teacherapp/create.html'
    success_url = reverse_lazy('update_teacher')


class teacherUpdateview(UpdateView):
    model = Teacher
    fields = ['branch','subject','image']
    template_name = 'update.html'

    def get_success_url(self):
        return reverse_lazy('detail_teacher', kwargs={'pk': self.object.id})

class teacherDetailview(DetailView):
    model =Teacher
    template_name = 'detail.html'

