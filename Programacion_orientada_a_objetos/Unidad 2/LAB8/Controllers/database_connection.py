"""PostgreSQL connection used by the application models."""

import psycopg
from psycopg import Error

from Controllers.config import DB_CONFIG


class DatabaseConnection:
    """Creates and checks connections to the application's PostgreSQL database."""

    def connect(self):
        try:
            return psycopg.connect(**DB_CONFIG)
        except Error as error:
            print(f"No se pudo conectar con PostgreSQL: {error}")
            return None

    def check_connection(self):
        """Open and close a connection, returning whether the check succeeded."""
        connection = self.connect()
        if connection is None:
            return False

        try:
            connected = connection.execute("SELECT 1").fetchone() == (1,)
            if connected:
                print("Conexión con PostgreSQL establecida correctamente.")
            return connected
        except Error as error:
            print(f"Falló la prueba de PostgreSQL: {error}")
            return False
        finally:
            connection.close()


if __name__ == "__main__":
    if not DatabaseConnection().check_connection():
        raise SystemExit(1)
