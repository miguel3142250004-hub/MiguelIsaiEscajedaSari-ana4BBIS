"""Connects login and registration views to the user model."""

import tkinter as tk

from Views.register_view import RegisterView


class AuthenticationController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.register_view = None

        self.view.btn_login.configure(command=self.login)
        self.view.btn_register.configure(command=self.open_registration)
        self.view.root.protocol("WM_DELETE_WINDOW", self.close_application)

    def login(self):
        email, password = self.view.get_data()
        if not email or not password:
            self.view.show_message(
                "Campos vacíos", "Ingresa el correo y la contraseña.", "error"
            )
            return

        user = self.model.validate_user(email, password)
        if user is None:
            self.view.show_message(
                "Error de conexión",
                "No fue posible consultar la base de datos. "
                "Verifica que PostgreSQL esté iniciado y configurado.",
                "error",
            )
        elif user is False:
            self.view.show_message(
                "Acceso denegado", "Correo o contraseña incorrectos.", "error"
            )
        else:
            _user_id, name = user
            self.view.show_message("Acceso correcto", f"Bienvenido, {name}.")
            self.view.clear_fields()

    def open_registration(self):
        if (
            self.register_view is not None
            and self.register_view.window.winfo_exists()
        ):
            self.register_view.window.lift()
            self.register_view.window.focus_force()
            return

        self.register_view = RegisterView(self.view.root)
        self.register_view.btn_save.configure(command=self.register_user)
        self.register_view.window.protocol(
            "WM_DELETE_WINDOW", self.close_registration
        )

    def register_user(self):
        name, email, password, confirmation = self.register_view.get_data()
        if not name or not email or not password or not confirmation:
            self.register_view.show_message(
                "Campos vacíos", "Todos los campos son obligatorios.", "error"
            )
            return

        if "@" not in email or "." not in email.rsplit("@", 1)[-1]:
            self.register_view.show_message(
                "Correo inválido", "Ingresa un correo electrónico válido.", "error"
            )
            return

        if password != confirmation:
            self.register_view.show_message(
                "Contraseñas diferentes", "Las contraseñas no coinciden.", "error"
            )
            return

        result = self.model.register_user(name, email, password)
        if result == "ok":
            self.register_view.show_message(
                "Registro exitoso", "El usuario se registró correctamente."
            )
            self.close_registration()
            self.view.entry_email.delete(0, tk.END)
            self.view.entry_email.insert(0, email)
        elif result == "duplicado":
            self.register_view.show_message(
                "Correo existente", "Ya existe una cuenta con ese correo.", "error"
            )
        else:
            self.register_view.show_message(
                "Error de base de datos",
                "No fue posible registrar al usuario. Verifica la conexión con PostgreSQL.",
                "error",
            )

    def close_registration(self):
        if self.register_view is not None:
            if self.register_view.window.winfo_exists():
                self.register_view.close()
            self.register_view = None

    def close_application(self):
        self.close_registration()
        self.view.root.destroy()
