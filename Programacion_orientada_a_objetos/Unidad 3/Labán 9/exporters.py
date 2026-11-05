"""Estrategias polimórficas para exportar inventario a archivos."""

from abc import ABC, abstractmethod
from datetime import date, datetime
from decimal import Decimal
import csv
import json

from fpdf import FPDF


class Exporter(ABC):
    """Interfaz común para todos los formatos de exportación."""

    CAMPOS = ("id", "nombre", "precio", "stock")

    @abstractmethod
    def export(self, data, file_path):
        """Guarda los productos en el formato de la clase hija."""
        raise NotImplementedError("La clase hija debe implementar export().")

    @classmethod
    def _normalizar_producto(cls, product):
        """Convierte una fila del modelo (diccionario o tupla) en diccionario."""
        if isinstance(product, dict):
            return {field: product.get(field) for field in cls.CAMPOS}
        return dict(zip(cls.CAMPOS, product))

    @classmethod
    def _normalizar_datos(cls, data):
        return [cls._normalizar_producto(product) for product in data]

    @staticmethod
    def _decimal_a_texto(value):
        # Mantiene todos los decimales de MySQL, útil para no redondear precios.
        return format(value, "f") if isinstance(value, Decimal) else value

    @staticmethod
    def _json_default(value):
        if isinstance(value, Decimal):
            return float(value)
        if isinstance(value, (date, datetime)):
            return value.isoformat()
        raise TypeError(f"Tipo no compatible con JSON: {type(value).__name__}")

    @staticmethod
    def _texto_pdf(value):
        """Adapta texto a las fuentes integradas de FPDF (Latin-1)."""
        return str(value).encode("latin-1", "replace").decode("latin-1")


class CSVExporter(Exporter):
    def export(self, data, file_path):
        productos = self._normalizar_datos(data)
        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=self.CAMPOS,
                extrasaction="ignore",
            )
            writer.writeheader()
            for producto in productos:
                writer.writerow({
                    campo: self._decimal_a_texto(producto.get(campo))
                    for campo in self.CAMPOS
                })
        return file_path


class TXTExporter(Exporter):
    def export(self, data, file_path):
        productos = self._normalizar_datos(data)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write("--- REPORTE DE PRODUCTOS ---\n")
            file.write(f"Productos registrados: {len(productos)}\n\n")
            for producto in productos:
                precio = self._decimal_a_texto(producto.get("precio"))
                file.write(
                    f"ID: {producto.get('id')} | "
                    f"Nombre: {producto.get('nombre')} | "
                    f"Precio: ${precio} | "
                    f"Stock: {producto.get('stock')}\n"
                )
        return file_path


class JSONExporter(Exporter):
    def export(self, data, file_path):
        productos = self._normalizar_datos(data)
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(
                productos,
                file,
                ensure_ascii=False,
                indent=4,
                default=self._json_default,
            )
            file.write("\n")
        return file_path


class PDFExporter(Exporter):
    def export(self, data, file_path):
        productos = self._normalizar_datos(data)
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()

        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, self._texto_pdf("Reporte de inventario"), ln=1, align="C")
        pdf.ln(4)

        pdf.set_font("Arial", "", 11)
        pdf.cell(0, 8, self._texto_pdf(f"Productos registrados: {len(productos)}"), ln=1)
        pdf.ln(2)

        if not productos:
            pdf.multi_cell(0, 8, self._texto_pdf("No hay productos para exportar."))

        for producto in productos:
            precio = self._decimal_a_texto(producto.get("precio"))
            pdf.set_font("Arial", "B", 11)
            pdf.multi_cell(
                0,
                7,
                self._texto_pdf(
                    f"ID: {producto.get('id')} | Nombre: {producto.get('nombre')}"
                ),
            )
            pdf.set_font("Arial", "", 10)
            pdf.cell(
                0,
                7,
                self._texto_pdf(f"Precio: ${precio} | Stock: {producto.get('stock')}"),
                ln=1,
            )
            pdf.ln(3)

        pdf.output(str(file_path))
        return file_path


_EXPORTERS = {
    "CSV": CSVExporter,
    "TXT": TXTExporter,
    "JSON": JSONExporter,
    "PDF": PDFExporter,
}


def create_exporter(file_format):
    """Crea la estrategia que corresponde al formato seleccionado."""
    normalized_format = str(file_format).strip().upper()
    try:
        exporter_class = _EXPORTERS[normalized_format]
    except KeyError as error:
        valid_formats = ", ".join(_EXPORTERS)
        raise ValueError(f"Formato no válido. Usa uno de estos: {valid_formats}.") from error
    return exporter_class()

