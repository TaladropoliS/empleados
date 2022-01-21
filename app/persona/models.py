from django.db import models
from app.departamento.models import Departamento
from ckeditor.fields import RichTextField

op_trabajo = [('CONTADOR', 'CONTADOR'),
              ('ADMINISTRADOR', 'ADMINISTRADOR'),
              ('ECONOMISTA', 'ECONOMISTA'),
              ('OTRO', 'OTRO')]


class Habilidades(models.Model):
    habilidad = models.CharField(max_length=60, verbose_name='Habilidad')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} - {self.habilidad}'

    class Meta:
        ordering = ['habilidad']
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'
        # unique_together = ('')


class Empleado(models.Model):
    departamento = models.ForeignKey(Departamento, related_name='empleado_departamento', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=60, verbose_name='Nombre')
    apellidos = models.CharField(max_length=60, unique=True, verbose_name='Apellidos')
    trabajo = models.CharField(choices=op_trabajo, max_length=60, verbose_name='Trabajo')
    activo = models.BooleanField(default=True, verbose_name='Activo')
    # foto = models.ImageField()
    habilidades = models.ManyToManyField(Habilidades, related_name='empleado_habilidades')
    hoja_de_vida = RichTextField()  # ckeditor, ya está instalado an las app e importado arrriba

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} - {self.nombre} {self.apellidos} - {self.departamento.nombre_corto}'

    class Meta:
        ordering = ['apellidos']
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        unique_together = ('nombre', 'apellidos')
