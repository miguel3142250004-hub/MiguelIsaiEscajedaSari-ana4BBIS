from Controller.database_connection import Database_connection


class Usuario:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.db = Database_connection()

    def autenticar(self):
        query = "SELECT id_user, username, nombre FROM users WHERE username = %s AND passw = %s"
        resultado = self.db.ejecutar_consulta(query, (self.username, self.password))

        if resultado:
            return resultado[0]
        return None
