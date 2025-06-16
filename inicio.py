from tkinter import *
from tkinter import messagebox
from datetime import datetime

# -----------------------
# VARIABLES GLOBALES
# -----------------------
productos = []
historial_ventas = []
nombre_usuario = ""

# -----------------------
# FUNCIONES PRINCIPALES
# -----------------------
def abrir_menu_principal():
    global nombre_usuario
    nombre_usuario = entrada_nombre.get()
    if not nombre_usuario:
        messagebox.showwarning("Campo vacío", "Por favor escribe el nombre o negocio")
        return
    ventana_inicio.destroy()
    mostrar_menu_principal()

def mostrar_menu_principal():
    global ventana_menu
    ventana_menu = Tk()
    ventana_menu.title("MiniInventario")
    ventana_menu.geometry("420x430")

    Label(ventana_menu, text="MiniInventario", font=("Arial", 16, "bold")).pack(pady=10)
    Label(ventana_menu, text=f"Bienvenido {nombre_usuario}", font=("Arial", 12)).pack(pady=10)

    Button(ventana_menu, text="➕ Ingresar Producto", width=30, command=mostrar_ingreso).pack(pady=6)
    Button(ventana_menu, text="💰 Vender Producto", width=30, command=mostrar_venta).pack(pady=6)
    Button(ventana_menu, text="❌ Eliminar Producto", width=30, command=mostrar_eliminacion).pack(pady=6)
    Button(ventana_menu, text="📦 Ver Salidas de Inventario", width=30, command=mostrar_historial).pack(pady=6)
    Button(ventana_menu, text="🔒 Cerrar sesión", width=30, bg="#f44336", fg="white", command=volver_al_inicio).pack(pady=15)

def volver_al_inicio():
    ventana_menu.destroy()
    main()

# -----------------------
# INGRESAR PRODUCTO
# -----------------------
def mostrar_ingreso():
    ventana_menu.withdraw()
    ingreso = Toplevel()
    ingreso.title("Ingresar Producto")
    ingreso.geometry("400x350")

    Label(ingreso, text="Nombre del Producto:").pack()
    entrada_nombre_p = Entry(ingreso, width=30)
    entrada_nombre_p.pack()

    Label(ingreso, text="Cantidad:").pack()
    entrada_cantidad = Entry(ingreso, width=30)
    entrada_cantidad.pack()

    Label(ingreso, text="Precio:").pack()
    entrada_precio = Entry(ingreso, width=30)
    entrada_precio.pack()

    lista = Listbox(ingreso, width=50)
    lista.pack(pady=10)

    def guardar_producto():
        nombre = entrada_nombre_p.get()
        try:
            cantidad = int(entrada_cantidad.get())
            precio = float(entrada_precio.get())
        except:
            messagebox.showerror("Error", "Cantidad y precio deben ser números")
            return

        if nombre:
            fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            productos.append({"nombre": nombre, "cantidad": cantidad, "precio": precio, "fecha_ingreso": fecha})
            actualizar_lista(lista)
            entrada_nombre_p.delete(0, END)
            entrada_cantidad.delete(0, END)
            entrada_precio.delete(0, END)
        else:
            messagebox.showwarning("Campo vacío", "Escribe el nombre del producto")

    Button(ingreso, text="Guardar Producto", command=guardar_producto).pack()
    Button(ingreso, text="Volver", command=lambda: [ingreso.destroy(), ventana_menu.deiconify()]).pack(pady=5)

    actualizar_lista(lista)

# -----------------------
# VENDER PRODUCTO
# -----------------------
def mostrar_venta():
    ventana_menu.withdraw()
    venta = Toplevel()
    venta.title("Vender Producto")
    venta.geometry("400x350")

    Label(venta, text="Selecciona el producto a vender").pack()

    lista = Listbox(venta, width=50)
    lista.pack(pady=10)

    def vender():
        seleccion = lista.curselection()
        if seleccion:
            index = seleccion[0]
            producto = productos[index]
            if producto["cantidad"] > 0:
                producto["cantidad"] -= 1
                fecha_venta = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                historial_ventas.append(f"{producto['nombre']} vendido por ${producto['precio']:.2f} | Fecha: {fecha_venta}")
                if producto["cantidad"] == 0:
                    productos.pop(index)
                actualizar_lista(lista)
            else:
                messagebox.showinfo("Sin stock", "Este producto no tiene unidades.")
        else:
            messagebox.showinfo("Selecciona algo", "Debes seleccionar un producto.")

    Button(venta, text="💸 Vender Uno", command=vender).pack()
    Button(venta, text="Volver", command=lambda: [venta.destroy(), ventana_menu.deiconify()]).pack(pady=5)

    actualizar_lista(lista)

# -----------------------
# ELIMINAR PRODUCTO
# -----------------------
def mostrar_eliminacion():
    ventana_menu.withdraw()
    eliminar = Toplevel()
    eliminar.title("Eliminar Producto")
    eliminar.geometry("400x300")

    Label(eliminar, text="Selecciona el producto a eliminar").pack()

    lista = Listbox(eliminar, width=50)
    lista.pack(pady=10)

    def eliminar_producto():
        seleccion = lista.curselection()
        if seleccion:
            index = seleccion[0]
            productos.pop(index)
            actualizar_lista(lista)
        else:
            messagebox.showinfo("Selecciona algo", "Debes seleccionar un producto.")

    Button(eliminar, text="🗑 Eliminar Producto", command=eliminar_producto).pack()
    Button(eliminar, text="Volver", command=lambda: [eliminar.destroy(), ventana_menu.deiconify()]).pack(pady=5)

    actualizar_lista(lista)

# -----------------------
# VER HISTORIAL DE VENTAS
# -----------------------
def mostrar_historial():
    ventana_menu.withdraw()
    salida = Toplevel()
    salida.title("Salidas de Inventario")
    salida.geometry("400x300")

    Label(salida, text="🧾 Historial de Ventas").pack()
    lista = Listbox(salida, width=50)
    lista.pack(pady=10)

    for venta in historial_ventas:
        lista.insert(END, venta)

    Button(salida, text="Volver", command=lambda: [salida.destroy(), ventana_menu.deiconify()]).pack(pady=5)

# -----------------------
# ACTUALIZAR LISTA
# -----------------------
def actualizar_lista(lista_widget):
    lista_widget.delete(0, END)
    for p in productos:
        texto = f"{p['nombre']} | Cant: {p['cantidad']} | ${p['precio']:.2f} | Ingresado: {p['fecha_ingreso']}"
        lista_widget.insert(END, texto)

# -----------------------
# VENTANA DE INICIO
# -----------------------
def main():
    global ventana_inicio, entrada_nombre
    ventana_inicio = Tk()
    ventana_inicio.title("MiniInventario")
    ventana_inicio.geometry("380x250")

    Label(ventana_inicio, text="MiniInventario", font=("Arial", 16, "bold")).pack(pady=10)
    Label(ventana_inicio, text="Escribe tu nombre o el de tu negocio:", font=("Arial", 11)).pack(pady=10)

    entrada_nombre = Entry(ventana_inicio, width=30)
    entrada_nombre.pack()

    Button(ventana_inicio, text="Iniciar", command=abrir_menu_principal).pack(pady=20)

    ventana_inicio.mainloop()

# -----------------------
# INICIAR APP
# -----------------------
main()
