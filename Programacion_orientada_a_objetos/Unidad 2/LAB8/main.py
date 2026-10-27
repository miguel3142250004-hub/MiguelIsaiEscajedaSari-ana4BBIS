"""Application entry point."""

import getpass
import os
import tkinter as tk


def main():
    # Ask in the terminal so the database password is not stored in the source.
    if not os.getenv("DB_PASSWORD"):
        os.environ["DB_PASSWORD"] = getpass.getpass(
            "Contraseña de PostgreSQL (usuario postgres): "
        )

    # Import after setting DB_PASSWORD because config.py reads it at import time.
    from Controllers.authentication_controller import AuthenticationController
    from Models.user_model import UserModel
    from Views.login_view import LoginView

    root = tk.Tk()
    view = LoginView(root)
    model = UserModel()
    AuthenticationController(model, view)
    root.mainloop()


if __name__ == "__main__":
    main()
