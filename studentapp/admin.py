from django.contrib import admin

# Register your models here.
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','user']  # Fields to show in list view
    # search_fields = ['subject_name']
admin.site.register(Student, StudentAdmin)
