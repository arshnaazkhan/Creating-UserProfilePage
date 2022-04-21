from django.contrib import admin
from .models import Profile
# Register your models here.
@admin.register(Profile)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name','email','date_of_birth','Contact_No','profile_pic']