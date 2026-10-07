import os
import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod


FONT_FAMILY = "Segoe UI"
FONT_TITLE = (FONT_FAMILY, 20, "bold")
FONT_GROUP = (FONT_FAMILY, 12, "bold")
FONT_OPTION = (FONT_FAMILY, 12)
FONT_BUTTON = (FONT_FAMILY, 12, "bold")
FONT_OUTPUT_INIT = (FONT_FAMILY, 11, "italic")
FONT_OUTPUT = (FONT_FAMILY, 12, "bold")

COLOR_BG = "#1e1e2e"
COLOR_CARD = "#2a2a3d"
COLOR_TITLE = "#f5c2e7"
COLOR_TEXT = "#cdd6f4"
COLOR_ACCENT = "#89b4fa"
COLOR_ACCENT_HOVER = "#74c7ec"
COLOR_BTN_TEXT = "#11111b"
COLOR_OUTPUT_BG = "#11111b"
COLOR_OUTPUT_FG = "#a6e3a1"


class SmartDevice(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def turn_on(self) -> str:
        pass


class Light(SmartDevice):
    def __init__(self):
        super().__init__("Light")

    def turn_on(self) -> str:
        return f"{self.name} is now ON. Brightening the room!"

    def turn_off(self) -> str:
        return f"{self.name} is now OFF. Dimming the room."


class TV(SmartDevice):
    def __init__(self):
        super().__init__("TV")

    def turn_on(self) -> str:
        return f"{self.name} is now ON. Enjoy your favorite shows!"

    def turn_off(self) -> str:
        return f"{self.name} is now OFF. See you next time!"

    def change_channel(self, channel: int) -> str:
        return f"{self.name} channel changed to {channel}. Enjoy watching!"

    def volume_up(self) -> str:
        return f"{self.name} volume increased. Louder sound!"

    def volume_down(self) -> str:
        return f"{self.name} volume decreased. Quieter sound."


class AirConditioner(SmartDevice):
    def __init__(self):
        super().__init__("Air Conditioner")

    def turn_on(self) -> str:
        return f"{self.name} is now ON. Cooling the room!"

    def turn_off(self) -> str:
        return f"{self.name} is now OFF. Warming the room."

    def set_temperature(self, temperature: int) -> str:
        return f"{self.name} temperature set to {temperature}°C. Comfortable environment!"


class PolymorphicAppTemplate(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Lab 6: Polymorphism with GUI")
        self.geometry("560x480")
        self.resizable(False, False)
        self.configure(bg=COLOR_BG)

        current_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(current_dir, "app_icon.png")

        if os.path.exists(icon_path):
            self.app_icon = tk.PhotoImage(file=icon_path)
            self.iconphoto(False, self.app_icon)
        else:
            print("Warning: Icon file 'app_icon.png' not found. Using default icon.")

        self.items = {
            "Light": Light(),
            "TV": TV(),
            "Air Conditioner": AirConditioner(),
        }

        self._configure_styles()
        self._build_interface()

    def _configure_styles(self):
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure(
            "Smart.TRadiobutton",
            background=COLOR_CARD,
            foreground=COLOR_TEXT,
            font=FONT_OPTION,
            focuscolor=COLOR_CARD,
            indicatorcolor=COLOR_OUTPUT_BG,
            padding=4,
        )
        style.map(
            "Smart.TRadiobutton",
            background=[("active", COLOR_CARD)],
            foreground=[("active", COLOR_ACCENT), ("selected", COLOR_ACCENT)],
            indicatorcolor=[("selected", COLOR_ACCENT)],
        )

    def _build_interface(self):
        lbl_header = tk.Label(
            self,
            text="🏠  Smart Home Center",
            font=FONT_TITLE,
            bg=COLOR_BG,
            fg=COLOR_TITLE,
        )
        lbl_header.pack(pady=(22, 12))

        group_box = tk.LabelFrame(
            self,
            text=" Select an Option ",
            font=FONT_GROUP,
            bg=COLOR_CARD,
            fg=COLOR_ACCENT,
            bd=2,
            relief="groove",
            padx=20,
            pady=14,
        )
        group_box.pack(fill="x", padx=30, pady=8)

        first_key = list(self.items.keys())[0]
        self.selected_key = tk.StringVar(value=first_key)

        for key in self.items.keys():
            rb = ttk.Radiobutton(
                group_box,
                text=key,
                value=key,
                variable=self.selected_key,
                style="Smart.TRadiobutton",
            )
            rb.pack(anchor="w", pady=4)

        self.btn_action = tk.Button(
            self,
            text="⚡  Turn On Device",
            command=self._handle_action,
            bg=COLOR_ACCENT,
            fg=COLOR_BTN_TEXT,
            activebackground=COLOR_ACCENT_HOVER,
            activeforeground=COLOR_BTN_TEXT,
            font=FONT_BUTTON,
            relief="flat",
            bd=0,
            cursor="hand2",
            padx=24,
            pady=10,
        )
        self.btn_action.pack(pady=18)

        self.btn_action.bind("<Enter>", lambda e: self.btn_action.config(bg=COLOR_ACCENT_HOVER))
        self.btn_action.bind("<Leave>", lambda e: self.btn_action.config(bg=COLOR_ACCENT))

        self.lbl_output = tk.Label(
            self,
            text="Select an option above and click 'Turn On Device'.",
            font=FONT_OUTPUT_INIT,
            bg=COLOR_OUTPUT_BG,
            fg=COLOR_TEXT,
            relief="flat",
            height=4,
            wraplength=480,
            justify="center",
        )
        self.lbl_output.pack(fill="x", padx=30, pady=8)

    def _handle_action(self):
        chosen_key = self.selected_key.get()
        active_object: SmartDevice = self.items[chosen_key]
        result_message = active_object.turn_on()
        self.lbl_output.config(
            text=result_message,
            font=FONT_OUTPUT,
            fg=COLOR_OUTPUT_FG,
        )


if __name__ == "__main__":
    app = PolymorphicAppTemplate()
    app.mainloop()