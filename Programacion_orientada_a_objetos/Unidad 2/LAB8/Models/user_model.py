"""Database operations for application users."""

import psycopg

from Controllers.database_connection import DatabaseConnection


class UserModel:
    def __init__(self):
        self.database = DatabaseConnection()

    def register_user(self, name, email, password):
        connection = self.database.connect()
        if connection is None:
            return "error"

        cursor = None
        try:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO users (nombre, email, password) VALUES (%s, %s, %s)",
                (name, email, password),
            )
            connection.commit()
            return "ok"
        except psycopg.IntegrityError:
            connection.rollback()
            return "duplicado"
        except psycopg.Error as error:
            connection.rollback()
            print(f"Error al registrar usuario: {error}")
            return "error"
        finally:
            if cursor is not None:
                cursor.close()
            connection.close()

    def validate_user(self, email, password):
        """Return (id, name), False for invalid credentials, or None on DB error."""
        connection = self.database.connect()
        if connection is None:
            return None

        cursor = None
        try:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT id, nombre FROM users WHERE email = %s AND password = %s",
                (email, password),
            )
            user = cursor.fetchone()
            return user if user is not None else False
        except psycopg.Error as error:
            print(f"Error al validar usuario: {error}")
            return None
        finally:
            if cursor is not None:
                cursor.close()
            connection.close()
