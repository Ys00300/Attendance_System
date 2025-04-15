# Register your models here.

from django.contrib import admin
from .models import Subject ,Attendance, StudentTeacher

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('course_code', 'subject_name', 'teachers')  # Fields to show in list view
    search_fields = ['subject_name']
admin.site.register(Subject, SubjectAdmin)



class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('status', 'date', 'student_teacher')  # Fields to show in list view
    # search_fields = ['subject_name']
    
    def student_name(self, obj):
        return obj.student_teacher.student.get_full_name()

    def subject_name(self, obj):
        return obj.student_teacher.subject.subject_name
    
admin.site.register(Attendance, AttendanceAdmin)



class StudentTeacherAdmin(admin.ModelAdmin):
    list_display = ('student', 'teacher', 'subject')  # Fields to show in list view
    # search_fields = ['subject_name']
admin.site.register(StudentTeacher, StudentTeacherAdmin)
