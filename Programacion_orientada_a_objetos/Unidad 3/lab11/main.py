"""Programa principal: retiro de productos del inventario.

Laboratorio 11
Autor: MIGUEL ISAI ESCAJEDA SARIÑANA
"""

from exceptions import ErrorInventario
from inventory import Inventario


def main() -> None:
    inventario = Inventario()

    codigo = input("Código del producto: ").strip()

    try:
        cantidad = int(input("Cantidad a retirar: "))
        inventario.retirar(codigo, cantidad)
    except ValueError:
        print("La cantidad debe ser un número entero.")
    except ErrorInventario as error:
        print(f"No se pudo realizar la operación: {error}")
    else:
        stock = inventario.obtener(codigo).stock
        print(f"Retiro realizado. Stock restante: {stock}")


if __name__ == "__main__":
    main()
