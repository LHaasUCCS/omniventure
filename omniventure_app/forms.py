from django import forms
from .models import *

class member_form(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        exclude = ['is_active']
        
