from tkinter import *
from tkinter import messagebox
from datetime import datetime

class Producto:
    def __init__(self, nombre, cantidad, precio, fecha_ingreso):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.fecha_ingreso = fecha_ingreso

    def __str__(self):
        return f"{self.nombre} | Cant: {self.cantidad} | ${self.precio:.2f} | Ingresado: {self.fecha_ingreso}"


class MiniInventarioApp:
    def __init__(self):
        self.productos = []
        self.historial_ventas = []
        self.nombre_usuario = ""
        self.ventana_inicio = None
        self.ventana_menu = None

        self.iniciar_app()

    def iniciar_app(self):
        self.ventana_inicio = Tk()
        self.ventana_inicio.title("MiniInventario")
        self.ventana_inicio.geometry("380x250")

        Label(self.ventana_inicio, text="MiniInventario", font=("Arial", 16, "bold")).pack(pady=10)
        Label(self.ventana_inicio, text="Escribe tu nombre o el de tu negocio:", font=("Arial", 11)).pack(pady=10)

        self.entrada_nombre = Entry(self.ventana_inicio, width=30)
        self.entrada_nombre.pack()

        Button(self.ventana_inicio, text="Iniciar", command=self.abrir_menu_principal).pack(pady=20)

        self.ventana_inicio.mainloop()

    def abrir_menu_principal(self):
        self.nombre_usuario = self.entrada_nombre.get()
        if not self.nombre_usuario:
            messagebox.showwarning("Campo vacío", "Por favor escribe el nombre o negocio")
            return
        self.ventana_inicio.destroy()
        self.mostrar_menu_principal()

    def mostrar_menu_principal(self):
        self.ventana_menu = Tk()
        self.ventana_menu.title("MiniInventario")
        self.ventana_menu.geometry("420x430")

        Label(self.ventana_menu, text="MiniInventario", font=("Arial", 16, "bold")).pack(pady=10)
        Label(self.ventana_menu, text=f"Bienvenido {self.nombre_usuario}", font=("Arial", 12)).pack(pady=10)

        Button(self.ventana_menu, text="➕ Ingresar Producto", width=30, command=self.mostrar_ingreso).pack(pady=6)
        Button(self.ventana_menu, text="💰 Vender Producto", width=30, command=self.mostrar_venta).pack(pady=6)
        Button(self.ventana_menu, text="❌ Eliminar Producto", width=30, command=self.mostrar_eliminacion).pack(pady=6)
        Button(self.ventana_menu, text="📦 Ver Salidas de Inventario", width=30, command=self.mostrar_historial).pack(pady=6)
        Button(self.ventana_menu, text="🔒 Cerrar sesión", width=30, bg="#f44336", fg="white", command=self.reiniciar).pack(pady=15)

    def reiniciar(self):
        self.ventana_menu.destroy()
        self.__init__()

    def mostrar_ingreso(self):
        self.ventana_menu.withdraw()
        ingreso = Toplevel()
        ingreso.title("Ingresar Producto")
        ingreso.geometry("400x350")

        Label(ingreso, text="Nombre del Producto:").pack()
        entrada_nombre = Entry(ingreso, width=30)
        entrada_nombre.pack()

        Label(ingreso, text="Cantidad:").pack()
        entrada_cantidad = Entry(ingreso, width=30)
        entrada_cantidad.pack()

        Label(ingreso, text="Precio:").pack()
        entrada_precio = Entry(ingreso, width=30)
        entrada_precio.pack()

        lista = Listbox(ingreso, width=50)
        lista.pack(pady=10)

        def guardar_producto():
            nombre = entrada_nombre.get()
            try:
                cantidad = int(entrada_cantidad.get())
                precio = float(entrada_precio.get())
            except:
                messagebox.showerror("Error", "Cantidad y precio deben ser números")
                return

            if nombre:
                fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                nuevo = Producto(nombre, cantidad, precio, fecha)
                self.productos.append(nuevo)
                self.actualizar_lista(lista)
                entrada_nombre.delete(0, END)
                entrada_cantidad.delete(0, END)
                entrada_precio.delete(0, END)
            else:
                messagebox.showwarning("Campo vacío", "Escribe el nombre del producto")

        Button(ingreso, text="Guardar Producto", command=guardar_producto).pack()
        Button(ingreso, text="Volver", command=lambda: [ingreso.destroy(), self.ventana_menu.deiconify()]).pack(pady=5)

        self.actualizar_lista(lista)

    def mostrar_venta(self):
        self.ventana_menu.withdraw()
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
                producto = self.productos[index]
                if producto.cantidad > 0:
                    producto.cantidad -= 1
                    fecha_venta = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    self.historial_ventas.append(f"{producto.nombre} vendido por ${producto.precio:.2f} | Fecha: {fecha_venta}")
                    if producto.cantidad == 0:
                        self.productos.pop(index)
                    self.actualizar_lista(lista)
                else:
                    messagebox.showinfo("Sin stock", "Este producto no tiene unidades.")
            else:
                messagebox.showinfo("Selecciona algo", "Debes seleccionar un producto.")

        Button(venta, text="💸 Vender Uno", command=vender).pack()
        Button(venta, text="Volver", command=lambda: [venta.destroy(), self.ventana_menu.deiconify()]).pack(pady=5)

        self.actualizar_lista(lista)

    def mostrar_eliminacion(self):
        self.ventana_menu.withdraw()
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
                self.productos.pop(index)
                self.actualizar_lista(lista)
            else:
                messagebox.showinfo("Selecciona algo", "Debes seleccionar un producto.")

        Button(eliminar, text="🗑 Eliminar Producto", command=eliminar_producto).pack()
        Button(eliminar, text="Volver", command=lambda: [eliminar.destroy(), self.ventana_menu.deiconify()]).pack(pady=5)

        self.actualizar_lista(lista)

    def mostrar_historial(self):
        self.ventana_menu.withdraw()
        salida = Toplevel()
        salida.title("Salidas de Inventario")
        salida.geometry("400x300")

        Label(salida, text="🧾 Historial de Ventas").pack()
        lista = Listbox(salida, width=50)
        lista.pack(pady=10)

        for venta in self.historial_ventas:
            lista.insert(END, venta)

        Button(salida, text="Volver", command=lambda: [salida.destroy(), self.ventana_menu.deiconify()]).pack(pady=5)

    def actualizar_lista(self, lista_widget):
        lista_widget.delete(0, END)
        for p in self.productos:
            lista_widget.insert(END, str(p))


# Iniciar la app
MiniInventarioApp()
