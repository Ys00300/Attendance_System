from django.contrib import admin
from django.contrib import admin
from .models import Teacher
# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','subject']
# Register your models here.


admin.site.register(Teacher,TeacherAdmin)