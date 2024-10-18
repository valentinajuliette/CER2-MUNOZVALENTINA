from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .models import Carrito, Producto, DetallePedido
from .forms import RegistroForm, PedidoForm
from django.contrib import messages

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

def pag_principal(request):
    productos = Producto.objects.all()  # Obtener todos los productos
    return render(request, 'pag_principal.html', {'productos': productos})

def catalogo_productos(request):
    return render(request, 'catalogo_productos.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('pag_principal')  # Redirige a la página principal después del login.
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'login.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('login')

def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito_item, created = Carrito.objects.get_or_create(user=request.user, producto=producto)
    if not created:
        carrito_item.cantidad += 1
    carrito_item.save()
    return redirect('ver_carrito')

def ver_carrito(request):
    carrito_items = Carrito.objects.filter(user=request.user)
    total = 0
    for item in carrito_items:
        # Calcular el total por cada producto (precio * cantidad)
        item.total = item.producto.precio * item.cantidad
        total += item.total  # Sumar el total de cada producto al total general

    return render(request, 'carrito.html', {
        'carrito_items': carrito_items,
        'total_carrito': total  # Pasar el total del carrito al contexto
    })

def eliminar_del_carrito(request, item_id):
    item = get_object_or_404(Carrito, id=item_id, user=request.user)
    item.delete()
    return redirect('ver_carrito')

def actualizar_carrito(request):
    if request.method == 'POST':
        # Itera a través de todos los items en el carrito del usuario.
        carrito_items = Carrito.objects.filter(user=request.user)
        for item in carrito_items:
            cantidad = request.POST.get(f'cantidad_{item.id}')
            if cantidad:
                # Actualiza la cantidad solo si es un número positivo.
                item.cantidad = max(int(cantidad), 1)
                item.save()
        return redirect('ver_carrito')

def finalizar_compra(request):
    carrito_items = Carrito.objects.filter(user=request.user)
    if request.method == 'POST':
    # Si el método es POST, se valida el formulario y se crea un nuevo Pedido.
        form = PedidoForm(request.POST)
        if form.is_valid():
            # Crear el pedido
            pedido = form.save(commit=False)
            pedido.user = request.user
            pedido.save()
            
            # Se guardan los detalles del pedido (DetallePedido) usando los productos que estaban en el carrito.
            for item in carrito_items:
                DetallePedido.objects.create(
                    pedido=pedido,
                    producto=item.producto,
                    cantidad=item.cantidad,
                    precio=item.producto.precio
                )
                # Actualizar stock del producto
                item.producto.stock = (item.producto.stock - item.cantidad)
                item.producto.save()  # Guardar los cambios en el stock
            
            # Vaciar el carrito después de finalizar la compra
            carrito_items.delete()
            
            # Pasar el mensaje de éxito
            return render(request, 'finalizar_compra.html', {
                'form': PedidoForm(),  # Limpiar el formulario
                'exito': 1,  # El pedido se registró con éxito
                'carrito_items': carrito_items
            })
        else:
            # En caso de que el formulario no sea válido
            return render(request, 'finalizar_compra.html', {
                'form': form,
                'exito': 0,  # Hubo un problema al registrar el pedido
                'carrito_items': carrito_items
            })
    else:
        form = PedidoForm()

    return render(request, 'finalizar_compra.html', {'form': form, 'carrito_items': carrito_items})