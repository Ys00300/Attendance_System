from django.shortcuts import render,redirect, get_object_or_404
from .models import Teacher
from django.views.generic.edit import CreateView ,UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from .forms import CustomUserForm, TeacherForm, SubjectForm
from finalAttendance.models import Subject
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.utils import timezone
from django.views import View
from finalAttendance.models import Attendance, StudentTeacher
from teacherapp.models import Teacher
from AttendanceSystem.models import CustomUser
from django.views.generic import ListView
from finalAttendance.models import Subject, StudentTeacher, Attendance
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class CreateTeacherView(LoginRequiredMixin,CreateView):
    model = Teacher
    fields = ['branch','subject','image']
    template_name = 'teacherapp/create.html'
    success_url = reverse_lazy('update-teacher')
    
    
class TeacherUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserForm
    template_name = 'updateTeacher.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object

        teacher, _ = Teacher.objects.get_or_create(user=user)
        subject = Subject.objects.filter(teachers=teacher).first()

        if self.request.method == 'POST':
            context['teacher_form'] = TeacherForm(self.request.POST, self.request.FILES, instance=teacher)
            context['subject_form'] = SubjectForm(self.request.POST, instance=subject)
        else:
            context['teacher_form'] = TeacherForm(instance=teacher)
            context['subject_form'] = SubjectForm(instance=subject)

        return context

    def form_valid(self, form):
        context = self.get_context_data()
        teacher_form = context['teacher_form']
        subject_form = context['subject_form']

        if teacher_form.is_valid() and subject_form.is_valid():
            self.object = form.save()

            teacher = teacher_form.save(commit=False)
            teacher.user = self.object
            teacher.save()

            subject = subject_form.save(commit=False)
            subject.teachers = teacher  # Link subject to teacher
            subject.save()

            return redirect(self.get_success_url())

        return self.form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('teacher_details', kwargs={'pk': self.object.pk})


class TeacherDetailview(LoginRequiredMixin,DetailView):
    
    model = CustomUser
    template_name = 'detailTeacher.html'

class MarkAttendanceView(LoginRequiredMixin, View):
    template_name = 'mark_attendance.html'
    
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            teacher = self.request.user.teacher 
             
            context['subject'] = Subject.objects.filter(teachers=teacher)
            return context
    
    def get(self, request, pk):
        
        teacher = get_object_or_404(Teacher, user=request.user)
        subject = get_object_or_404(Subject, id=pk, teachers=teacher)
        student_teacher_links = StudentTeacher.objects.filter(teacher=teacher, subject=subject)
        
        context = {
            'subject': subject,
            'student_teacher_links': student_teacher_links,
            'today': timezone.now().date()
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        teacher = get_object_or_404(Teacher, user=request.user)
        subject = get_object_or_404(Subject, id=pk, teachers=teacher)
        student_teacher_links = StudentTeacher.objects.filter(teacher=teacher, subject=subject)
        attendance_date = timezone.now().date()

        for link in student_teacher_links:
            status = request.POST.get(f'status_{link.id}')
            if status:
                Attendance.objects.update_or_create(
                    student_teacher=link,
                    date=attendance_date,
                    defaults={'status': status}
                )

        messages.success(request, 'Attendance has been saved successfully.')
        return redirect('teacherHome')  
    
