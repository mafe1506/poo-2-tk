import tkinter as tk
from tkinter import messagebox

class InfoPopup(object):
    def show_info_message(self):
        messagebox.showinfo("Información", "Este es un mensaje informativo.")

class WarningPopup(object):
    def show_warning_message (self):
        messagebox.showwarning("Advertencia", "Este es un mensaje de advertencia.")

class CombinedPopup(InfoPopup, WarningPopup):
     def show_both_messages(self):
        self.show_info_message()
        self.show_warning_message()
         #Se puede utilizar polimorfismo para mostrar el mensaje de cualquier clase hija que herede de InfoPopup o WarningPopup


root = tk.Tk()
root.withdraw()
#Se crean instancias
combined_popup = CombinedPopup()
combined_popup.show_both_messages()
#se inicia el loop
root.mainloop()