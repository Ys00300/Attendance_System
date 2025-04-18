from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['id','username', 'email', 'gender', 'section', 'branch', 'en_Number', 'date_of_creation','profile_image']
    list_filter = ['is_staff', 'is_superuser', 'gender', 'section']
    search_fields = ['username', 'email', 'en_Number']
    ordering = ['username']
    
# admin.site.register(CustomUser,CustomUserAdmin) also use to register the model at admin panel
