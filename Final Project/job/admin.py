from django.contrib import admin

from .models import  User

# Register your models here.
  

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "usericon")
    list_filter = ("usericon",)
    search_fields = ("username", "userphonenumber", "usericon")
    ordering = ("username", "usericon")
