from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile

#Formulario para editar usuario existentes
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('sex', 'location', 'birth_date')


#Formulario para crear nuevos usuarios
class FormSignUp(UserCreationForm):
    SEX_CHOICES = (
        ('Hombre', 'Hombre'),
        ('Mujer', 'Mujer'),
    )
    first_name = forms.CharField(max_length=140, required=True)
    last_name = forms.CharField(max_length=140, required=False)
    email = forms.EmailField(required=True)
    location = forms.CharField(max_length=140, required=False)
    birth_date = forms.DateField (required=False)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',   
	        'location',
	        'birth_date',
            'password1',
            'password2',
        )
