from django.db import models


class Departamento(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    nombre_corto = models.CharField(max_length=20, unique=True, verbose_name='Nombre Corto')
    no_activo = models.BooleanField(default=False, verbose_name='No Activo')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # editable=False permite bloquear la edición del campo en el Admin.

    def __str__(self):
        return f'{self.id} - {self.nombre} - {self.nombre_corto}'

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Dapertamento'
        verbose_name_plural = 'Dapertamentos'

        # unique_together no permite que se creen combinaciones iguales,
        # en este caso 'entre nombre' y 'nombre_corto'.
        unique_together = ('nombre', 'nombre_corto')
