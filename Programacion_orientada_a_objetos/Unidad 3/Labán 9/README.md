# Práctica de Laboratorio 9: Módulo de Exportación

Esta práctica extiende el MVC de productos del Laboratorio 7 para exportar el inventario de MySQL a CSV, TXT, JSON y PDF.

## Preparación

Desde esta carpeta, crea y activa un entorno virtual e instala las dependencias:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Configura MySQL con el script `Models/database_squema.sql`. Si tu instalación usa otros datos de conexión, actualiza `Controller/config.py`.

## Ejecución

```powershell
python Main.py
```

Inicia sesión con los datos de usuario definidos en el script SQL. En el panel, selecciona CSV, TXT, JSON o PDF, pulsa **Exportar reporte** y elige dónde guardar el archivo.

## Estructura de exportación

Las clases `CSVExporter`, `TXTExporter`, `JSONExporter` y `PDFExporter` heredan de `Exporter` y sobrescriben `export()`. El controlador obtiene los productos, elige la estrategia correspondiente y llama al mismo método `export()` para todos los formatos. Las librerías `csv`, `json` y `fpdf` se usan únicamente en `exporters.py`.

