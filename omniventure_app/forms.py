from django import forms
from .models import *

class member_form(forms.ModelForm):
    class Meta:
        model = Member
        exclude = ['is_active', 'user']  # Exclude these fields from the form

    # Explicitly include the image field
    image = forms.ImageField(label='Image', required=False)

class CharacterForm(forms.ModelForm):
    character_id = forms.IntegerField(label="Character ID")
    background = forms.CharField(max_length=2000, label='Background')
    personality = forms.CharField(max_length=200, label='Personality')
    pronouns = forms.CharField(max_length=100, label='Pronouns')

    class Meta:
        model = Character
        fields = ['character_id', 'background', 'personality', 'pronouns']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
