from django.contrib import admin
from .models import Addstudent
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ["name","roll_number","address","instagram_link"]

admin.site.register(Addstudent,StudentAdmin)