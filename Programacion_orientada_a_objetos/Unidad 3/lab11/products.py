"""Modelo de producto del inventario.

Laboratorio 11
Autor: MIGUEL ISAI ESCAJEDA SARIÑANA
"""

from exceptions import CantidadInvalida, StockInsuficiente


class Producto:
    """Representa un producto identificado por código, con su stock."""

    def __init__(self, codigo: str, stock: int) -> None:
        self.codigo = codigo
        self.stock = stock

    def retirar(self, cantidad: int) -> None:
        """Descuenta `cantidad` unidades del stock.

        Raises:
            CantidadInvalida: si la cantidad es menor o igual a cero.
            StockInsuficiente: si la cantidad excede el stock disponible.
        """
        if cantidad <= 0:
            raise CantidadInvalida("La cantidad a retirar debe ser mayor a cero.")

        if cantidad > self.stock:
            raise StockInsuficiente(
                f"Stock insuficiente para '{self.codigo}': "
                f"disponible {self.stock}, solicitado {cantidad}."
            )

        self.stock -= cantidad

    def __repr__(self) -> str:
        return f"Producto(codigo={self.codigo!r}, stock={self.stock})"
