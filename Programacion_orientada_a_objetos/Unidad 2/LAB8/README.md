# Lab 8 — Login MVC (PostgreSQL)

## Archivos y arquitectura

- `Controllers/database_connection.py`: abre y verifica conexiones PostgreSQL.
- `Controllers/config.py`: configuración de conexión, ajustable mediante variables de entorno.
- `Controllers/authentication_controller.py`: enlaza las acciones de las vistas con el modelo.
- `Models/user_model.py`: registra usuarios y valida credenciales.
- `Models/database_schema.sql`: crea la tabla `users` dentro de la base seleccionada.
- `Views/login_view.py`: ventana de inicio de sesión.
- `Views/register_view.py`: ventana de registro.
- `main.py`: construye y ejecuta la aplicación.

## Preparar y ejecutar

1. Inicia el servicio de PostgreSQL.
2. En pgAdmin, crea la base de datos `login_mvc`, selecciónala, abre **Query Tool** y ejecuta `Models/database_schema.sql`.
3. Instala la dependencia con `python -m pip install -r requirements.txt`.
4. Al iniciar `main.py`, escribe en la terminal la contraseña de PostgreSQL cuando se solicite; no se mostrará ni se guardará en el código. También puedes definir `DB_PASSWORD` en el entorno. Si tu instalación usa otros valores, configura `DB_HOST`, `DB_USER`, `DB_NAME` o `DB_PORT`; los valores iniciales son `localhost`, usuario `postgres`, base `login_mvc` y puerto `5432`.
5. Desde esta carpeta, ejecuta `python main.py`.

Para probar la conexión a PostgreSQL desde esta carpeta, ejecuta `python -m Controllers.database_connection`. El comando termina con código 0 si conecta y código 1 si falla.
