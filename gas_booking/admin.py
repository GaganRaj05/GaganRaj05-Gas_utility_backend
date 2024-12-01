from django.contrib import admin
from .models import User,Services

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'username','password')  

class UserRequests(admin.ModelAdmin):
    list_display = ('file','service_type','description',"username","status")

admin.site.register(User, UserAdmin) 
admin.site.register(Services,UserRequests)




