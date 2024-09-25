import tkinter as tk
from tkinter import messagebox

class ErrorPopup:
    def show_error(self):
        messagebox.showerror("Error", "Ha ocurrido un error.")
class CustomErrorPopup(ErrorPopup):
    def show_error(self):
        messagebox.showerror("Error Personalizado", "Ha ocurrido un error en la aplicación. Por favor, contacte con el administrador.")


root = tk.Tk()
root.withdraw()
ErrPopup = ErrorPopup()
CustomErrPopup = CustomErrorPopup()

ErrPopup.show_error()
CustomErrPopup.show_error()

root.mainloop()