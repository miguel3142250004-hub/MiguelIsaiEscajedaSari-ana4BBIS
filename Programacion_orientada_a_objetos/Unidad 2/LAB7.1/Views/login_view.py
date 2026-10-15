import tkinter as tk
from tkinter import messagebox
from Models import Usuario
from Views.home_view import DashboardVentana

class LoginVentana:
    """Ventana de inicio de sesión."""

    def __init__(self, root):
        self.root = root
        self.root.title("Acceso al Sistema")
        self.root.geometry("350x380")
        self.root.resizable(False, False)

        # Construir la interfaz
        self._crear_interfaz()

    def _crear_logo(self):
        canvas = tk.Canvas(
            self.root, width=90, height=80,
            bg=self.root.cget("bg"), highlightthickness=0
        )
        canvas.pack(pady=(20, 0))

        # Monitor
        canvas.create_rectangle(10, 8, 80, 55, fill="#2196F3", outline="#1565C0", width=2)
        # Pantalla
        canvas.create_rectangle(16, 14, 74, 49, fill="#E3F2FD", outline="")
        # Icono de usuario dentro de la pantalla
        canvas.create_oval(39, 19, 51, 31, fill="#1565C0", outline="")
        canvas.create_arc(32, 32, 58, 58, start=0, extent=180, fill="#1565C0", outline="")
        # Soporte y base
        canvas.create_rectangle(40, 55, 50, 66, fill="#1565C0", outline="")
        canvas.create_rectangle(28, 66, 62, 71, fill="#1565C0", outline="")

    def _crear_interfaz(self):
        # Título
        lbl_titulo = tk.Label(self.root, text="Iniciar Sesión", font=("Helvetica", 16, "bold"))
        lbl_titulo.pack(pady=25)

        self._crear_logo()

        # Campo Usuario
        lbl_usuario = tk.Label(self.root, text="Usuario:", font=("Helvetica", 10))
        lbl_usuario.pack(anchor="w", padx=30, pady=(5, 2))
        
        self.entry_usuario = tk.Entry(self.root, font=("Helvetica", 11))
        self.entry_usuario.pack(fill="x", padx=30)

        # Campo Contraseña
        lbl_pass = tk.Label(self.root, text="Contraseña:", font=("Helvetica", 10))
        lbl_pass.pack(anchor="w", padx=30, pady=(15, 2))
        
        self.entry_pass = tk.Entry(self.root, font=("Helvetica", 11), show="*")
        self.entry_pass.pack(fill="x", padx=30)

        # Botón Ingresar
        btn_ingresar = tk.Button(
            self.root, 
            text="Entrar", 
            font=("Helvetica", 11, "bold"),
            bg="#2196F3", 
            fg="white", 
            cursor="hand2",
            command=self._validar_login
        )
        btn_ingresar.pack(fill="x", padx=30, pady=30)

    def _validar_login(self):
        usuario_texto = self.entry_usuario.get().strip()
        pass_texto = self.entry_pass.get().strip()

        # Validación básica de campos vacíos
        if not usuario_texto or not pass_texto:
            messagebox.showwarning("Campos Vacíos", "Por favor ingresa usuario y contraseña.")
            return

        # Instanciar el modelo Usuario y autenticar
        usuario_obj = Usuario(usuario_texto, pass_texto)
        datos_usuario = usuario_obj.autenticar()

        if datos_usuario:
            messagebox.showinfo("Bienvenido", f"¡Hola {datos_usuario['nombre']}! Acceso concedido.")
            self._abrir_dashboard(datos_usuario['nombre'])
        else:
            messagebox.showerror("Error de Acceso", "Usuario o contraseña incorrectos.")

    def _abrir_dashboard(self, nombre_completo):
    
        self.root.destroy()
        root_dashboard = tk.Tk()
        DashboardVentana(root_dashboard, nombre_completo)
        root_dashboard.mainloop()

