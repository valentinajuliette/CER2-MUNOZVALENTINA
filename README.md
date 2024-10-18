# Proyecto para Certamen 1 del ramo "Taller de Lenguajes de Programación"

**Alumna**: Valentina Juliette Muñoz Rabanal  
**Carrera**: Ingeniería en Informática (2do año)

---

## Descripción del Proyecto

**"Tienda Verde"** es una pequeña empresa dedicada a la venta de productos ecológicos que busca mejorar la gestión de su inventario mediante una aplicación web. Esta aplicación permitirá a los administradores manejar los productos de la tienda utilizando un modelo de desarrollo en capas y un Framework ORM para interactuar con la base de datos.

### Funcionalidades Acordadas

| **Código** | **Requerimiento**                                                                                     |
|------------|-------------------------------------------------------------------------------------------------------|
| REQ01      | El sitio debe ser construido utilizando Django Framework.                                              |
| REQ02      | Debe considerar un Frontend basado en Bootstrap Framework, utilizando templates heredados.             |
| REQ03      | El sistema debe permitir navegar por todas las funcionalidades, solicitando iniciar sesión cuando sea necesario. |
| REQ04      | El usuario superadministrador debe poder gestionar las tablas maestras del sistema (vía Django Admin). |
| REQ05      | El usuario superadministrador debe poder administrar cuentas de vendedores y asignar restricciones (vía Django Admin). |
| REQ06      | El cliente debe poder registrarse en la tienda usando su correo electrónico.                           |
| REQ07      | El cliente autenticado debe poder agregar productos al carrito de compras.                             |
| REQ08      | El cliente autenticado debe poder eliminar productos del carrito.                                      |
| REQ09      | El cliente autenticado debe poder ver el carrito, el total a pagar y confirmar el pedido.              |
| REQ10      | El vendedor debe poder ver el listado de pedidos realizados y filtrarlos por estado (pendiente o completado). |
| REQ11      | El vendedor debe poder cambiar el estado de un pedido de pendiente a completado.                       |

---

## Sistema de Roles

| **Rol**               | **Permisos y Restricciones**                                                                | **Interfaz**        |
|-----------------------|---------------------------------------------------------------------------------------------|---------------------|
| **Cliente Anónimo**    | • Navegar por el sitio web.                                                                 | Sitio Web           |
|                       | • Registrarse en la tienda.                                                                 |                     |
| **Cliente Registrado** | • Navegar por el sitio web.                                                                 | Sitio Web           |
|                       | • Iniciar sesión, agregar y eliminar productos del carrito de compras.                       |                     |
|                       | • Cerrar sesión.                                                                            |                     |
| **Vendedor**           | • Ver el listado de pedidos realizados y cambiar su estado.                                 | Django Admin        |
| **Superadministrador** | • Mantener el catálogo de productos y gestionar usuarios.                                    | Django Admin        |

---

## Condiciones Especiales

| **Código** | **Requerimiento**                                                                                     |
|------------|-------------------------------------------------------------------------------------------------------|
| REQ06      | Validar que el usuario no se haya registrado previamente.                                              |
| REQ07      | En esta evaluación se permitirá ingresar solo una unidad de cada producto. Actualizar el total del carrito. |
| REQ08      | Al eliminar productos del carrito, se debe actualizar el total a pagar.                                |
