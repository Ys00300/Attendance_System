from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .models import Attendance, StudentTeacher

class AttendanceListView(LoginRequiredMixin, TemplateView):
    template_name = 'attendance_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        
        if hasattr(user, 'teacher'):
            teacher = user.teacher
            context['role'] = 'teacher'
            context['attendance_list'] = Attendance.objects.filter(
                student_teacher__teacher=teacher
            )


        elif hasattr(user, 'student'):
            student = user.student
            context['role'] = 'student'
         
            context['attendance_list'] = Attendance.objects.filter(
                student_teacher__student=student
            )
        else:
           
            context['attendance_list'] = []
            context['role'] = 'unknown'

        return context
