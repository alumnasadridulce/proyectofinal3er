#Proyecto Final
#submodulo 
#Autor:Adriana y Dulce 

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk # Necesita instalar pillow: pip install pillow
import os
# -------------------------
# FUNCIONES (pantallas vacías por ahora)
# -------------------------
def abrir_registro_productos():
    messagebox.showinfo("Registro de Productos", "Aquí irá el módulo de registro de productos.")

def abrir_registro_ventas():
    messagebox.showinfo("Registro de Ventas", "Aquí irá el módulo de registro de ventas.")

def abrir_reportes():
    messagebox.showinfo("Reportes", "Aquí irá el módulo de reportes.")

def abrir_acerca_de():
    messagebox.showinfo("Acerca de", "Punto de Venta de Ropa\nProyecto Escolar\nVersión 1.0")

# -------------------------
# VENTANA PRINCIPAL
# -------------------------
ventana = tk.Tk()
ventana.title("Software 2025")
ventana.geometry("500x600")
ventana.resizable(False, False)
ventana.configure(bg="#F5F5DC")

# -------------------------
# LOGO
# -------------------------
try:
   BASE_DIR = os.path.dirname(os.path.abspath(__file__))
   imagen = Image.open(os.path.join(BASE_DIR,"ventas2025.jpeg")) # Cambia por el archivo del alumno
   imagen = imagen.resize((250, 250)) # Tamaño recomendado
   img_logo = ImageTk.PhotoImage(imagen)

   lbl_logo = tk.Label(ventana, image=img_logo)
   lbl_logo.pack(pady=20)
except:
   lbl_sin_logo = tk.Label(ventana, text="(Aquí va el logo del sistema)", font=("Arial", 14))
   lbl_sin_logo.pack(pady=40)

# -------------------------
# BOTONES PRINCIPALES (COLOR + LETRA + MISMO TAMAÑO)
# -------------------------

ESTILO_BOTON = {
    "font": ("Arial", 12),
    "bg": "#6A0DAD",     # Púrpura
    "fg": "white",       # Letra blanca
    "activebackground": "#540a85",
    "activeforeground": "white",
    "width": 25,         # MISMO TAMAÑO
    "height": 2
}

btn_reg_prod = tk.Button(ventana, text="Registro de Productos", command=abrir_registro_productos, **ESTILO_BOTON)
btn_reg_prod.pack(pady=10)

btn_reg_ventas = tk.Button(ventana, text="Registro de Ventas", command=abrir_registro_ventas, **ESTILO_BOTON)
btn_reg_ventas.pack(pady=10)

btn_reportes = tk.Button(ventana, text="Reportes", command=abrir_reportes, **ESTILO_BOTON)
btn_reportes.pack(pady=10)

btn_acerca = tk.Button(ventana, text="Acerca de", command=abrir_acerca_de, **ESTILO_BOTON)
btn_acerca.pack(pady=10)



# -------------------------
# INICIO DE LA APP
# -------------------------
ventana.mainloop()