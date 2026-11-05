"""Controlador que coordina el modelo de productos y la estrategia exportadora."""

from Models import Producto
from exporters import create_exporter


class ProductosController:
    def __init__(self, modelo=None):
        self.modelo = modelo if modelo is not None else Producto()

    def obtener_productos(self):
        return self.modelo.obtener_todos()

    def exportar_productos(self, formato, ruta_archivo):
        productos = self.modelo.obtener_todos()
        exporter = create_exporter(formato)
        return exporter.export(productos, ruta_archivo)

