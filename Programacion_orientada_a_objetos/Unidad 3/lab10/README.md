# Lab 10 - Automated Testing with pytest

## Estructura
```
lab10_pytest/
├── app_movil.py        # Lógica: excepciones, PerfilMovil, PerfilPro
├── test_app_movil.py   # Suite de pruebas pytest
├── test.py             # Investigación sobre pytest (comentarios)
├── requirements.txt
└── README.md
```

## Cómo ejecutar
```bash
# (Opcional) entorno virtual
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux / Mac

pip install -r requirements.txt
pytest -v
```
Toma la captura de pantalla de `pytest -v` con todos los tests en PASSED (evidencia de la práctica).
