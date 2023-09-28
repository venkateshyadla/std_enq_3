from django import forms
from .models import Enquiry

class Enquiryform(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['name','father_name','email','enquiry_date','dob','course','branch','std_id']