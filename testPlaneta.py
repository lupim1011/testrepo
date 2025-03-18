import tkinter as tk
from tkinter import messagebox 
from tkinter import simpledialog 
from Planeta import Planeta
root = tk.Tk()
root.withdraw()

messagebox.showinfo("TITULO","SISTEMA SOLAR")
planetita = Planeta()
    
planetita.nombre = simpledialog.askstring("Planeta","Nombre:") #input("Nombre: ")
planetita.masa = simpledialog.askfloat("","Masa:") #float(input("Masa: "))
planetita.volumen = simpledialog.askfloat("","Volumen:") #float(input("Volumen: "))
planetita.distancia = simpledialog.askfloat("","Distacia al Sol:")#float(input("Distancia al sol: "))



 
 messagebox.showinfo("",f"Su densidad es:{planetita.calcularDensidad()}")
messagebox.showinfo("","Es un planeta exterior" if planetita.esPlanetaExterior() else "No es un planeta exterior")

#if planetita.esPlanetaExterior():
#    print("Es un planeta exterior")
#else:
#    print("No es un planeta exterior")