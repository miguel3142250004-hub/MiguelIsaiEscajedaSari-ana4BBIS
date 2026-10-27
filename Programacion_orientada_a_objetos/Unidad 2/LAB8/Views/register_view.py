"""Registration dialog and its presentation-only helpers."""

import tkinter as tk
from tkinter import messagebox


class RegisterView:
    BG = "#EFF4FA"
    CARD = "#FFFFFF"
    TEXT = "#14213D"
    MUTED = "#64748B"
    PRIMARY = "#2563EB"
    PRIMARY_HOVER = "#1D4ED8"
    BORDER = "#D8E1ED"
    FIELD_BG = "#F8FAFC"

    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("Crear cuenta")
        self.window.geometry("480x650")
        self.window.configure(bg=self.BG)
        self.window.resizable(False, False)
        self.window.transient(root)
        self.window.grab_set()

        card = tk.Frame(self.window, bg=self.CARD, padx=40, pady=28)
        card.place(relx=0.5, rely=0.5, anchor="center", width=390)

        tk.Label(
            card,
            text="NUEVO USUARIO",
            font=("Segoe UI", 9, "bold"),
            bg=self.CARD,
            fg=self.PRIMARY,
        ).pack(anchor="w", pady=(0, 10))

        tk.Label(
            card,
            text="Crear cuenta",
            font=("Segoe UI", 22, "bold"),
            bg=self.CARD,
            fg=self.TEXT,
        ).pack(anchor="w")

        tk.Label(
            card,
            text="Completa tus datos para registrarte.",
            font=("Segoe UI", 10),
            bg=self.CARD,
            fg=self.MUTED,
        ).pack(anchor="w", pady=(4, 17))

        self.entry_name = self._add_field(card, "Nombre completo")
        self.entry_email = self._add_field(
            card, "Correo electrónico", top_padding=12
        )
        self.entry_password = self._add_field(
            card, "Contraseña", masked=True, top_padding=12
        )
        self.entry_confirmation = self._add_field(
            card, "Confirmar contraseña", masked=True, top_padding=12
        )

        self.btn_save = tk.Button(
            card,
            text="Registrar usuario",
            font=("Segoe UI", 11, "bold"),
            bg=self.PRIMARY,
            fg="#FFFFFF",
            activebackground=self.PRIMARY_HOVER,
            activeforeground="#FFFFFF",
            relief="flat",
            bd=0,
            cursor="hand2",
            pady=10,
        )
        self.btn_save.pack(fill="x", pady=(20, 9))
        self._add_hover(self.btn_save, self.PRIMARY, self.PRIMARY_HOVER)

        self.btn_cancel = tk.Button(
            card,
            text="Cancelar",
            font=("Segoe UI", 10, "bold"),
            bg=self.CARD,
            fg=self.MUTED,
            activebackground="#F1F5F9",
            activeforeground=self.TEXT,
            relief="flat",
            bd=0,
            highlightthickness=1,
            highlightbackground=self.BORDER,
            highlightcolor=self.BORDER,
            cursor="hand2",
            pady=8,
            command=self.close,
        )
        self.btn_cancel.pack(fill="x")
        self._add_hover(self.btn_cancel, self.CARD, "#F1F5F9")

        self.entry_name.focus_set()
        self.window.bind("<Return>", lambda _event: self.btn_save.invoke())

    def _add_field(self, parent, label, masked=False, top_padding=0):
        tk.Label(
            parent,
            text=label,
            bg=self.CARD,
            fg=self.TEXT,
            font=("Segoe UI", 10, "bold"),
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
        entry.pack(fill="x", ipady=9)
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
        return (
            self.entry_name.get().strip(),
            self.entry_email.get().strip(),
            self.entry_password.get(),
            self.entry_confirmation.get(),
        )

    def show_message(self, title, message, kind="info"):
        if kind == "error":
            messagebox.showerror(title, message, parent=self.window)
        else:
            messagebox.showinfo(title, message, parent=self.window)

    def close(self):
        self.window.destroy()
