Documentación del Sistema de Mini Inventario
Descripción General
Este programa implementa una interfaz gráfica (GUI) usando Tkinter para la gestión básica de un inventario de productos, registro de ventas y consulta de historial. Está diseñado para llevar el control de productos agregados, realizar ventas y mostrar registros históricos, todo de forma local.
Requisitos del Sistema
- Python 3.x
- Módulo tkinter (incluido con Python)
- Módulo datetime (incluido con Python)
Variables Globales
productos = []           # Lista que almacena los productos agregados
historial_ventas = []    # Lista que almacena las ventas realizadas
nombre_usuario = ""      # Nombre del usuario que ingresa al sistema
Funciones del Sistema
• abrir_menu_principal(): Abre la ventana principal del menú de operaciones una vez que el usuario ha iniciado sesión.
• registrar_producto(): Agrega nuevos productos al inventario, validando los campos.
• vender_producto(): Registra una venta y descuenta del inventario.
• mostrar_historial(): Muestra todas las ventas realizadas.
• inicio_sesion(): Pide el nombre del usuario.
• main(): Inicia la interfaz gráfica.
Estructura del Programa
main()
└── inicio_sesion()
    └── abrir_menu_principal()
        ├── registrar_producto()
        ├── vender_producto()
        └── mostrar_historial()
Validaciones
- Verifica campos vacíos al registrar productos o ventas.
- Manejo de errores con try-except.
- Muestra alertas con messagebox.
Formato del Historial de Ventas
{
  "producto": "Nombre del producto",
  "cantidad": 2,
  "fecha": "2025-06-16 10:20:30"
}
Ejemplo de Producto en Inventario
{
  "nombre": "Lápiz",
  "precio": 1000,
  "cantidad": 50
}
Tecnologías Utilizadas
- Python 3
- Tkinter
- datetime
- messagebox
Limitaciones del Sistema
- Datos no se guardan permanentemente.
- Sin autenticación segura.
- No permite edición ni eliminación.
Posibles Mejoras Futuras
- Guardar en archivos o bases de datos.
- Reportes por fecha.
- Autenticación con contraseña.
- Validaciones más robustas.
