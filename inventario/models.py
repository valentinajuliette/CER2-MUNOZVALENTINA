# Se crea un modelo que represente los productos en la tienda.
# Este modelo utilizará el ORM de Django para interactuar con la base de datos.

from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    nombre = models.CharField(max_length=255) # Nombre del producto.
    descripcion = models.TextField() # Breve descripción del producto.
    precio = models.IntegerField() # Precio del producto con dos decimales.
    stock = models.IntegerField() # Cantidad de este producto en inventario.
    categoria = models.CharField(max_length=100) # Categoría del producto (por ejemplo, "limpieza del hogar", "higiege personal").
    imagen = models.ImageField(upload_to='img/productos/', null=True, blank=True) # Campo para cargar la imagen del producto.

    def __str__(self):
        return self.nombre

class Carrito(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.producto.nombre} - {self.cantidad}"

class Pedido(models.Model):
    ESTADOS_PEDIDO = [
        ('pendiente', 'Pendiente'),
        ('completado', 'Completado'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre_cliente = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    direccion_entrega = models.CharField(max_length=255)
    numero_tarjeta = models.CharField(max_length=16)  # Aquí se guarda solo para fines de demostración (no recomendado para producción)
    codigo_cvv = models.CharField(max_length=4)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS_PEDIDO, default='pendiente')

    def __str__(self):
        return f"Pedido {self.id} de {self.user.username}"

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.producto.nombre} (x{self.cantidad}) - Pedido {self.pedido.id}"

