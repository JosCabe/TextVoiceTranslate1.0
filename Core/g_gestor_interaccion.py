import tkinter as tk
from tkinter import messagebox

class GestorInteraccion:
    """
    Clase que gestiona interacciones con el usuario (GUI o consola).
    """

    @staticmethod
    def preguntar_eliminacion():
        root = tk.Tk()
        root.withdraw()
        return messagebox.askyesno("Eliminar archivos", "¿Deseas eliminar los archivos generados?")
