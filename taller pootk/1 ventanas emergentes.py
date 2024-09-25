import tkinter as tk
from tkinter import messagebox

#  ventana principal
root = tk.Tk()
root.title("Ejemplo de PopupBase")

# Luego se crea la clase PopubBase  propuesta en el ejercicio de la clase
class PopupBase:
    def click(self):
        messagebox.showinfo("Mensaje informativo", "Bienvenido")
# clase hija custompopup
class CustomPopup(PopupBase):
    def click(self):
        messagebox.showinfo("Mensaje personalizado", "Felicitaciones")

#instancia para la clase principal
popup = PopupBase()

#  instancia de la clase hija
custom_popup = CustomPopup()

# botón y asociarlo al método click de la instancia popup
button = tk.Button(root, text="Click", command=popup.click)
button.pack(pady=10)

# Se crea otro botón y asociarlo al método click de la instancia de la clase hija
custom_button = tk.Button(root, text="Click personalizado", command=custom_popup.click)
custom_button.pack(pady=10)

# Iniciar el loop de la ventana
root.mainloop()

