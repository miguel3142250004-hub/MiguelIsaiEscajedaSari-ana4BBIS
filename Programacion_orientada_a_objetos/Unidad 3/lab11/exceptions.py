"""Excepciones personalizadas del sistema de inventario.

Laboratorio 11
Autor: MIGUEL ISAI ESCAJEDA SARIÑANA
"""


class ErrorInventario(Exception):
    """Excepción base para todos los errores del inventario."""


class ProductoNoEncontrado(ErrorInventario):
    """El código solicitado no existe en el inventario."""


class CantidadInvalida(ErrorInventario):
    """La cantidad indicada no es válida (cero o negativa)."""


class StockInsuficiente(ErrorInventario):
    """La cantidad solicitada supera el stock disponible."""
