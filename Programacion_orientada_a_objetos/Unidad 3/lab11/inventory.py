"""Gestión del inventario de productos.

Laboratorio 11
Autor: MIGUEL ISAI ESCAJEDA SARIÑANA
"""

from exceptions import ProductoNoEncontrado
from products import Producto

# Stock inicial por código de producto.
STOCK_INICIAL: dict[str, int] = {
    "P01": 5,
    "P02": 10,
    "P03": 8,
}


class Inventario:
    """Colección de productos indexados por su código."""

    def __init__(self) -> None:
        self.productos: dict[str, Producto] = {
            codigo: Producto(codigo, stock)
            for codigo, stock in STOCK_INICIAL.items()
        }

    def obtener(self, codigo: str) -> Producto:
        """Devuelve el producto o lanza ProductoNoEncontrado."""
        try:
            return self.productos[codigo]
        except KeyError:
            raise ProductoNoEncontrado(
                f"El producto con código '{codigo}' no existe."
            ) from None

    def retirar(self, codigo: str, cantidad: int) -> None:
        """Retira `cantidad` unidades del producto indicado."""
        self.obtener(codigo).retirar(cantidad)
