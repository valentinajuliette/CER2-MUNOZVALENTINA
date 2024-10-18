DESCRIPCIÓN DE PROYECTO PARA CERTAMEN 1 DEL RAMO "TALLER DE LENGUAJES DE PROGRAMACIÓN"
=====================================
Alumna: Valentina Juliette Muñoz Rabanal
2do año de Ingeniería en Informática
=====================================

"Tienda Verde", la pequeña empresa dedicada a la venta de productos ecológicos ha decidido mejorar la gestión de su
inventario utilizando una aplicación que permita a los administradores manejar los productos de la tienda. Esta
aplicación será desarrollada utilizando un modelo de desarrollo en capas y un Framework ORM para interactuar con la
base de datos que almacena la información de los productos.
Se ha reunido con los interesados del proyecto y en conjunto se ha acordado que la aplicación debe tener las siguientes
funcionalidades:

CÓDIGO - REQUERIMIENTO
REQ01 - El sitio debe ser construido utilizando Django Framework.
REQ02 - Debe considerar un Font End basado en Bootstrap Framework que utilice templates heredados en su construcción.
REQ03 - Desde la versión web, debe permitir navegar por todas las funcionalidades del sitio, solicitando iniciar sesión
cuando corresponda.
REQ04 - El sistema debe permitir a un usuario superadministrador (usando el módulo de administrador de Django) mantener
las tablas maestras del sistema.
REQ05 - El sistema debe permitir a un usuario superadministrador (usando el módulo de administrador de Django) administrar
cuentas para vendedores asignando las restricciones necesarias.
REQ06 - El sistema debe permitir a un usuario cliente, registrarse en la tienda usando su correo electrónico.
REQ07 - El sistema debe permitir a un usuario cliente correctamente autentificado, agregar productos de la tienda a un
carrito de compras.
REQ08 - El sistema debe permitir a un usuario cliente correctamente autentificado, eliminar productos desde su carrito de compras.
REQ09 - El sistema debe permitir a un usuario cliente correctamente autentificado, ver su carrito, el total a pagar y
confirmar su pedido.
REQ10 - El sistema debe permitir a un usuario vendedor, ver el listado completo de pedidos realizados pudiendo filtrar aquellos
que están pendientes de entregar (usando el módulo de administrador de Django).
REQ11 - El sistema debe permitir a un usuario vendedor cambiar el estadio de un pedido de pendiente a completado (usando el
módulo de administrador de Django).

--- SISTEMA DE ROLES ---
ROL                              PERMISOS Y RESTRICCIONES                                INTERFAZ
Cliente Anónimo             • Navegar por el sitio web de la tienda                      Sitio web
                            • Registrarse en la tienda 
Cliente Registrado          • Navegar por el sitio web de la tienda                      Sitio web
                            • Iniciar sesión en la tienda
                            • Agregar productos al carrito de compras
                            • Eliminar productos de su carrito de compras
                            • Cerrar sesión
Vendedor                    • Ver listado de pedidos realizados                           Django Admin
                            • Cambiar el estado de un pedido
Superadministrador          • Mantener el catálogo de productos
                            • Mantener los usuarios del sistema                           Django Admin

--- CONDICIONES ESPECIALES ---
CÓDIGO - REQUERIMIENTO
REQ06 - El sistema debe validar que el usuario no se haya registrado previamente.
REQ07 - Para esta evaluación se permitirá ingresar una unidad de cada producto. Considerar actualizar el total a pagar del carrito.
REQ08 - El sistema debe permitir a un usuario cliente correctamente autentificado, eliminar productos desde su carrito de compras.
Considerar actualizar el total a pagar del carrito.
