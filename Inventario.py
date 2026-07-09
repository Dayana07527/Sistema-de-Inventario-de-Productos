#Part- 2 code-screen
import tkinter as tk
from tkinter import ttk

def crear_pantalla_inventario(ventana):
    frame = tk.Frame(ventana)
    return frame


#IMPORTANDO A JSON
import json
with open("inventario.json", "r",
encoding="utf-8") as archivo:
    inventario = json.load(archivo)


#Creando la ventana
ventana = tk.Tk()
#color de la ventana
ventana.config(bg="#84E488")
ventana.title("Inventario de Productos")
ventana.geometry("1100x600")
ventana.state("zoomed")

boton_volver = tk.Button(
    ventana,
    text="← Volver",
    command = ventana,
    font=("Arial",11,"bold")   
)
boton_volver.pack(anchor="w" , padx=13, pady=8)


boton_volver.pack(pady=14)


# Crear tabla con diseño
style = ttk.Style()

style.theme_use("clam")

style.configure(
    "Treeview",
    background="white",
    foreground="black",
    rowheight=28,
    fieldbackground="white",
    font=("Arial",11)
)

style.configure(
    "Treeview.Heading",
    background="#2F698B",
    foreground="white",
    font=("Arial",11,"bold")
)



tabla = ttk.Treeview(ventana)

# Definir columnas
tabla["columns"] = ("Código", "Nombre", "Categoría", "Cantidad", "Precio")

# Ocultar la primera columna vacía
tabla.column("#0", width=0, stretch=tk.NO)

# Configurar columnas
tabla.column("Código", width=100, anchor="center")
tabla.column("Nombre", width=350)
tabla.column("Categoría", width=150, anchor="center")
tabla.column("Cantidad", width=100, anchor="center")
tabla.column("Precio", width=100, anchor="center")

# Encabezados
tabla.heading("#0", text="")
tabla.heading("Código", text="Código")
tabla.heading("Nombre", text="Nombre")
tabla.heading("Categoría", text="Categoría")
tabla.heading("Cantidad", text="Cantidad")
tabla.heading("Precio", text="Precio")

# Agregar productos a la tabla
for producto in inventario:
    tabla.insert(
        "",
        tk.END,
        values=(
            producto["codigo"],
            producto["nombre"],
            producto["categoria"],
            producto["cantidad"],
            f"${producto['precio']:.2f}"
        )
    )

# Mostrar tabla
tabla.pack(fill="both", expand=True, padx=10, pady=10)


# Ejecutar ventana
ventana.mainloop()