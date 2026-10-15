import tkinter as tk
from tkinter import ttk
from Models import Producto


class DashboardVentana:
    """Ventana principal después de iniciar sesión."""

    def __init__(self, root, nombre_usuario):
        self.root = root
        self.root.title("Panel Principal")
        self.root.geometry("600x400")

        lbl_mensaje = tk.Label(
            self.root,
            text=f"¡Bienvenido/a al Sistema!\nUsuario activo: {nombre_usuario}",
            font=("Helvetica", 12),
            justify="center"
        )
        lbl_mensaje.pack(pady=15)

        self._crear_tabla_productos()
        self._cargar_productos()

    def _crear_tabla_productos(self):
        lbl_titulo = tk.Label(self.root, text="Productos", font=("Helvetica", 14, "bold"))
        lbl_titulo.pack()

        columnas = ("id", "nombre", "precio", "stock")
        self.tabla = ttk.Treeview(self.root, columns=columnas, show="headings", height=10)

        self.tabla.heading("id", text="ID")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("precio", text="Precio")
        self.tabla.heading("stock", text="Stock")

        self.tabla.column("id", width=50, anchor="center")
        self.tabla.column("nombre", width=250)
        self.tabla.column("precio", width=120, anchor="e")
        self.tabla.column("stock", width=80, anchor="center")

        self.tabla.pack(fill="both", expand=True, padx=20, pady=10)

    def _cargar_productos(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        for p in Producto().obtener_todos():
            self.tabla.insert(
                "", "end",
                values=(p["id"], p["nombre"], f"{p['precio']:.2f}", p["stock"])
            )
