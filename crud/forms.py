from django import forms
from .models import Addstudent
class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Addstudent
        fields = ("name","roll_number","address","instagram_link")
