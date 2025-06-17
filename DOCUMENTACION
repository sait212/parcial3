 Documentación del Sistema MiniInventario (versión POO)
🧾 1. Descripción General
MiniInventario es una aplicación de escritorio desarrollada en Python con la biblioteca Tkinter, orientada a pequeños negocios o emprendimientos que necesiten llevar un control básico de su inventario. Esta versión del programa está estructurada siguiendo los principios de la Programación Orientada a Objetos (POO), lo que permite un diseño más limpio, reutilizable y mantenible.

🧱 2. Estructura de Clases
🔹 Clase Producto
Representa un producto almacenado en el inventario.

Atributos:

nombre (str): Nombre del producto.

cantidad (int): Cantidad disponible en stock.

precio (float): Precio por unidad del producto.

fecha_ingreso (str): Fecha y hora en que se ingresó el producto.

Métodos:

__str__(): Devuelve una cadena legible del producto con su información formateada.

🔹 Clase MiniInventarioApp
Contiene toda la lógica del sistema y la gestión de la interfaz gráfica.

Atributos principales:

productos (list): Lista de objetos Producto.

historial_ventas (list): Registro de ventas realizadas.

nombre_usuario (str): Nombre del usuario o negocio ingresado.

ventana_inicio, ventana_menu: Referencias a las ventanas de Tkinter.

Métodos principales:

Método	Función
__init__()	Inicializa atributos y lanza la app.
iniciar_app()	Muestra la ventana de inicio para ingresar el nombre del usuario.
abrir_menu_principal()	Guarda el nombre e inicia el menú principal.
mostrar_menu_principal()	Presenta las opciones del sistema: ingresar, vender, eliminar y ver historial.
reiniciar()	Reinicia la aplicación cerrando sesión.
mostrar_ingreso()	Ventana para ingresar nuevos productos.
mostrar_venta()	Permite vender un producto del inventario.
mostrar_eliminacion()	Permite eliminar un producto de la lista.
mostrar_historial()	Muestra las ventas realizadas.
actualizar_lista()	Actualiza visualmente las listas de productos.

🖥️ 3. Ventanas del Sistema
Ventana de inicio: Solicita el nombre del usuario o negocio.

Menú principal: Presenta botones para las funciones básicas.

Ingreso de producto: Formulario con Entry y Listbox para ingresar datos.

Venta de producto: Lista de productos disponibles, permite disminuir stock.

Eliminación de producto: Lista productos y permite su eliminación.

Historial de ventas: Muestra productos vendidos con precio y fecha.

✅ 4. Funcionamiento Interno
Al iniciar, el sistema solicita el nombre del usuario.

Luego se muestra el menú con las acciones posibles.

Todos los datos se almacenan en memoria usando listas (productos y historial_ventas).

No hay base de datos; los datos se pierden al cerrar la aplicación.

Se utiliza Listbox para mostrar los productos y ventas de forma visual.

El manejo de errores (como valores no numéricos) se hace con try-except y mensajes de alerta con messagebox.

🔧 5. Tecnologías Utilizadas
Lenguaje: Python 3

Biblioteca gráfica: Tkinter

Módulos adicionales: datetime para manejar fechas y horas

👨‍💻 6. Autoría y Uso
Este programa puede ser utilizado como base educativa para comprender conceptos de POO, interfaces gráficas con Tkinter y gestión básica de datos. Es ideal para estudiantes de programación, proyectos universitarios o negocios pequeños que deseen controlar su inventario de manera sencilla.

Fecha de documentación: Junio de 2025

