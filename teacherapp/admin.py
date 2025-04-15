from django.contrib import admin
from django.contrib import admin
from .models import Teacher
from finalAttendance.models import Subject
# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','user']
# Register your models here.



# class SubjectInline(admin.TabularInline):
#     model = Subject.teachers.through  # Many-to-many relation through model
#     extra = 1

# class TeacherAdmin(admin.ModelAdmin):
#     inlines = [SubjectInline]

admin.site.register(Teacher,TeacherAdmin)