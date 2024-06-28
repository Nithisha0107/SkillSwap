from django.contrib import admin

# Register your models here.
from .models import User 

class UserAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','username','password','email','phone_number','qualification','occupation','profile_picture']

admin.site.register(User,UserAdmin)