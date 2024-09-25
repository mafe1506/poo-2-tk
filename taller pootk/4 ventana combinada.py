#En primer lugar debemos importar tkinter
import tkinter as tk
from tkinter import messagebox

# Despues procedemos a crear la clase solicitada Infopopup
class InfoPopup:
    def show_message(self):
        messagebox.showinfo("Información", "Este es un mensaje informativo.")

# Siguiente de esto creamos una segunda clase solicitada
class ErrorPopup:
    def show_message(self):
        messagebox.showerror("Error", "Ha ocurrido un error.")

# Posteriormente Creamos la clase hija que hereda de ambas clases y sobrescribe el método
class CustomPopup(InfoPopup, ErrorPopup):
    def show_message(self):
        # Personalizamos los mensajes
        messagebox.showinfo("Información Importante", "Este es un mensaje informativo importante.")
        messagebox.showerror("Error importante", "Este es un mensaje de error importante.")

# Ocultamos la ventana principal de Tkinter para mejor visualizacion
root = tk.Tk()
root.withdraw()

# Y finalmente Creamos una instancia de CustomPopup y mostramos los mensajes
custom_popup = CustomPopup()
custom_popup.show_message()

root.mainloop()