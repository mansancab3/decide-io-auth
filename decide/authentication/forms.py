from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('sex', 'location', 'birth_date')
            
