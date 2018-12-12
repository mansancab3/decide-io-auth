from django import forms

from .models import Usuario


class UserCreationForm(forms.ModelForm):
    userForm = forms.CharField(max_length=50, label="Usuario")
    passWForm = forms.CharField(max_length=50, label="Password")
    nameUsuarioForm = forms.CharField(max_length=50, label="Nombre")
    surnameUsuarioForm = forms.CharField(max_length=50,label="Apellidos")
    genreUsuarioForm = forms.CharField(max_length=50, label="Genero")
    paisUsuarioForm = forms.CharField(max_length=50, label="Pais de Nacimiento")
    dateUsuarioForm = forms.CharField(max_length=50, label="Fecha de Nacimiento")
     
    class Meta:
        model=Usuario
        fields=()
          
    def save(self,commit=True):
        usuarioDecide = super(UserCreationForm,self).save(commit=False)
        usuarioDecide.user = self.cleaned_data["userForm"]
        usuarioDecide.passW = self.cleaned_data["passWForm"]
        usuarioDecide.nameUsuario = self.cleaned_data["nameUsuarioForm"]
        usuarioDecide.surnameUsuario = self.cleaned_data["surnameUsuarioForm"]
        usuarioDecide.genreUsuario = self.cleaned_data["genreUsuarioForm"]
        usuarioDecide.paisUsuario = self.cleaned_data["paisUsuarioForm"]
        usuarioDecide.dateUsuario = self.cleaned_data["dateUsuarioForm"]
        if commit: 
            usuarioDecide.save() 
        return usuarioDecide
             
