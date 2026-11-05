import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from Controller.productos_controller import ProductosController


class DashboardVentana:
    """Panel principal con inventario y opciones de exportación."""

    FORMATOS = ("CSV", "TXT", "JSON", "PDF")

    def __init__(self, root, nombre_usuario):
        self.root = root
        self.root.title("Panel Principal")
        self.root.geometry("700x460")
        self.root.minsize(620, 400)
        self.controlador = ProductosController()
        self.formato_exportacion = tk.StringVar(value=self.FORMATOS[0])

        lbl_mensaje = tk.Label(
            self.root,
            text=f"¡Bienvenido/a, {nombre_usuario}!",
            font=("Helvetica", 12),
        )
        lbl_mensaje.pack(pady=(14, 8))

        self._crear_controles_exportacion()
        self._crear_tabla_productos()
        self._cargar_productos()

    def _crear_controles_exportacion(self):
        panel = ttk.Frame(self.root)
        panel.pack(fill="x", padx=20, pady=(4, 10))

        ttk.Label(panel, text="Formato de exportación:").pack(side="left", padx=(0, 8))
        self.selector_formato = ttk.Combobox(
            panel,
            textvariable=self.formato_exportacion,
            values=self.FORMATOS,
            state="readonly",
            width=10,
        )
        self.selector_formato.pack(side="left")

        ttk.Button(
            panel,
            text="Exportar reporte",
            command=self._exportar_productos,
        ).pack(side="left", padx=12)

    def _crear_tabla_productos(self):
        ttk.Label(self.root, text="Productos", font=("Helvetica", 14, "bold")).pack()

        columnas = ("id", "nombre", "precio", "stock")
        self.tabla = ttk.Treeview(
            self.root,
            columns=columnas,
            show="headings",
            height=12,
        )

        self.tabla.heading("id", text="ID")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("precio", text="Precio")
        self.tabla.heading("stock", text="Stock")

        self.tabla.column("id", width=55, anchor="center")
        self.tabla.column("nombre", width=300)
        self.tabla.column("precio", width=130, anchor="e")
        self.tabla.column("stock", width=90, anchor="center")

        self.tabla.pack(fill="both", expand=True, padx=20, pady=(8, 16))

    def _cargar_productos(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        for producto in self.controlador.obtener_productos():
            precio = producto.get("precio")
            precio_mostrado = f"{float(precio):.2f}" if precio is not None else ""
            self.tabla.insert(
                "",
                "end",
                values=(
                    producto.get("id"),
                    producto.get("nombre"),
                    precio_mostrado,
                    producto.get("stock"),
                ),
            )

    def _exportar_productos(self):
        formato = self.formato_exportacion.get()
        extension = formato.lower()
        ruta_archivo = filedialog.asksaveasfilename(
            title="Exportar inventario",
            initialfile=f"productos.{extension}",
            defaultextension=f".{extension}",
            filetypes=(
                (f"{formato} (*.{extension})", f"*.{extension}"),
                ("Todos los archivos", "*.*"),
            ),
        )
        if not ruta_archivo:
            return

        try:
            self.controlador.exportar_productos(formato, ruta_archivo)
            messagebox.showinfo(
                "Exportación exitosa",
                f"El reporte se guardó en:\n{ruta_archivo}",
                parent=self.root,
            )
        except Exception as error:
            messagebox.showerror(
                "No se pudo exportar",
                str(error),
                parent=self.root,
            )

