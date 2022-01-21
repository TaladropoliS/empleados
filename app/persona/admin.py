from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.

admin.site.register(Habilidades)


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['departamento',
                    'full_name',  # full name no existe, pero se crea la funcion para que lo muestre
                    'nombre', 'apellidos',
                    'trabajo', 'activo',
                    'created_at', 'updated_at']  # No incluir ManyToManieFields

    search_fields = ['nombre', 'apellidos', 'trabajo']  # NO incluir datos foráneos (ningún tipo)
    # readonly_fields = ['']  # Solo lectura (no editable)
    list_filter = ['trabajo', 'departamento', 'habilidades']  # SI se pueden incluir datos foráneos
    list_editable = ['nombre', 'apellidos', 'activo']
    filter_horizontal = ('habilidades',)  # es para relaciones ManyToManieFields (tiene que ser una tupla con ,)
    list_per_page = 25

    def full_name(self, obj):
        return f'{obj.nombre} {obj.apellidos}'
