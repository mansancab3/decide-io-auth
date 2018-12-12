from django.db import models

# Create your models here.
class Usuario(models.Model):
    user = models.CharField(max_length=20)
    passW = models.CharField(max_length=20, verbose_name="Contraseña")
    nameUsuario = models.CharField(max_length=20, verbose_name="Nombre")
    surnameUsuario = models.CharField(max_length=40, verbose_name="Apellidos")
    genreUsuario = models.CharField(max_length=40,verbose_name="Genero")
    paisUsuario = models.CharField(max_length=40, verbose_name="Pais de origen")
    dateUsuario = models.CharField(max_length=40, verbose_name="Fecha de Nacimiento")
    
    def _self_(self):
        return self.user