"""Login window and its presentation-only helpers."""

import tkinter as tk
from tkinter import messagebox


class LoginView:
    BG = "#EFF4FA"
    CARD = "#FFFFFF"
    TEXT = "#14213D"
    MUTED = "#64748B"
    PRIMARY = "#2563EB"
    PRIMARY_HOVER = "#1D4ED8"
    BORDER = "#D8E1ED"
    FIELD_BG = "#F8FAFC"

    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de acceso")
        self.root.geometry("480x560")
        self.root.configure(bg=self.BG)
        self.root.resizable(False, False)

        card = tk.Frame(root, bg=self.CARD, padx=40, pady=34)
        card.place(relx=0.5, rely=0.5, anchor="center", width=390)

        tk.Label(
            card,
            text="LAB 8  ·  SISTEMA DE ACCESO",
            font=("Segoe UI", 9, "bold"),
            bg=self.CARD,
            fg=self.PRIMARY,
        ).pack(anchor="w", pady=(0, 12))

        tk.Label(
            card,
            text="Iniciar sesión",
            font=("Segoe UI", 23, "bold"),
            bg=self.CARD,
            fg=self.TEXT,
        ).pack(anchor="w")

        tk.Label(
            card,
            text="Ingresa tus datos para continuar.",
            font=("Segoe UI", 10),
            bg=self.CARD,
            fg=self.MUTED,
        ).pack(anchor="w", pady=(5, 24))

        self.entry_email = self._add_field(card, "Correo electrónico")
        self.entry_password = self._add_field(
            card, "Contraseña", masked=True, top_padding=17
        )

        self.btn_login = tk.Button(
            card,
            text="Ingresar",
            font=("Segoe UI", 11, "bold"),
            bg=self.PRIMARY,
            fg="#FFFFFF",
            activebackground=self.PRIMARY_HOVER,
            activeforeground="#FFFFFF",
            relief="flat",
            bd=0,
            cursor="hand2",
            pady=11,
        )
        self.btn_login.pack(fill="x", pady=(25, 10))
        self._add_hover(self.btn_login, self.PRIMARY, self.PRIMARY_HOVER)

        self.btn_register = tk.Button(
            card,
            text="Crear cuenta nueva",
            font=("Segoe UI", 10, "bold"),
            bg=self.CARD,
            fg=self.PRIMARY,
            activebackground="#EFF6FF",
            activeforeground=self.PRIMARY_HOVER,
            relief="flat",
            bd=0,
            highlightthickness=1,
            highlightbackground=self.BORDER,
            highlightcolor=self.BORDER,
            cursor="hand2",
            pady=9,
        )
        self.btn_register.pack(fill="x")
        self._add_hover(self.btn_register, self.CARD, "#EFF6FF")

        tk.Label(
            card,
            text="Tus datos se usarán para iniciar sesión en este sistema.",
            font=("Segoe UI", 8),
            bg=self.CARD,
            fg=self.MUTED,
            wraplength=290,
            justify="center",
        ).pack(pady=(22, 0))

        self.entry_email.focus_set()
        self.root.bind("<Return>", lambda _event: self.btn_login.invoke())

    def _add_field(self, parent, label, masked=False, top_padding=0):
        tk.Label(
            parent,
            text=label,
            font=("Segoe UI", 10, "bold"),
            bg=self.CARD,
            fg=self.TEXT,
        ).pack(anchor="w", pady=(top_padding, 7))

        entry = tk.Entry(
            parent,
            font=("Segoe UI", 11),
            bg=self.FIELD_BG,
            fg=self.TEXT,
            insertbackground=self.TEXT,
            relief="flat",
            bd=0,
            highlightthickness=1,
            highlightbackground=self.BORDER,
            highlightcolor=self.PRIMARY,
            show="*" if masked else "",
        )
        entry.pack(fill="x", ipady=10)
        return entry

    @staticmethod
    def _add_hover(button, normal_color, hover_color):
        button.bind(
            "<Enter>", lambda _event: button.configure(bg=hover_color)
        )
        button.bind(
            "<Leave>", lambda _event: button.configure(bg=normal_color)
        )

    def get_data(self):
        return self.entry_email.get().strip(), self.entry_password.get()

    def clear_fields(self):
        self.entry_email.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)

    def show_message(self, title, message, kind="info"):
        if kind == "error":
            messagebox.showerror(title, message, parent=self.root)
        else:
            messagebox.showinfo(title, message, parent=self.root)
