# Django ofrece una interfaz de administrador lista para usar, así que registramos el modelo en admin.py
# para gestionar los productos desde el panel de administrador.

from django.contrib import admin
from .models import Producto, Pedido, DetallePedido

admin.site.register(Producto)

class DetallePedidoInline(admin.TabularInline):
    model = DetallePedido
    extra = 0  # No añadir filas extra para detalles
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_cliente', 'telefono', 'direccion_entrega', 'fecha_pedido', 'user', 'estado')
    search_fields = ('nombre_cliente', 'telefono')
    list_filter = ('estado','fecha_pedido',)
    list_editable = ('estado',)  # Hacer el campo 'estado' editable desde la vista de lista
    date_hierarchy = 'fecha_pedido'
    inlines = [DetallePedidoInline]  # Mostrar detalles del pedido en la vista de Pedido

    # Sobrescribir el método get_readonly_fields para permitir solo la edición del campo 'estado' a los vendedores
    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='Vendedores').exists():
            return [f.name for f in self.model._meta.fields if f.name != 'estado']  # Todos los campos excepto 'estado' serán de solo lectura
        return super().get_readonly_fields(request, obj)

# Registrar el modelo Pedido con PedidoAdmin
admin.site.register(Pedido, PedidoAdmin)