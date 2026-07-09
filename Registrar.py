from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
import os

ARCHIVO_JSON = "registrar.json"
registro = []

def cargar_registrar():
    global registro
    if os.path.exists(ARCHIVO_JSON):
        try:
            with open(ARCHIVO_JSON, "r", encoding="utf-8") as archivo:
                registro = json.load(archivo)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el archivo: {e}")
            registro = []
    else:
        registro = []

def guardar_en_json():
    try:
        with open(ARCHIVO_JSON, "w", encoding="utf-8") as archivo:
            json.dump(registro, archivo, indent=4, ensure_ascii=False)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar en el archivo: {e}")


cargar_registrar()


def abrir_pantalla_registro(ventana_principal):
    """Función para integrar con el menú principal. 
    Oculta el menú y despliega esta interfaz."""
    global window
    
    
    ventana_principal.withdraw()

    window = tk.Toplevel(ventana_principal)
    window.title("Sistema de registro")
    window.geometry("1366x768")

    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)
    window.grid_columnconfigure(2, weight=1)

    
    window.protocol("WM_DELETE_WINDOW", lambda: volver_a_menu_principal(ventana_principal))

    letrero = tk.Label(window, text="Ingresa los datos:", font=("Arial", 40))
    letrero.grid(row=0, column=0, columnspan=3, pady=30)

    labelCodigo = tk.Label(window, text="Código del producto:", font=("Arial", 23))
    labelCodigo.grid(row=1, column=0, sticky="e", padx=(0,20), pady=10)
    input_codigo = tk.Entry(window, font=("Arial", 18), width=30)
    input_codigo.grid(row=1, column=1, sticky="w", padx=(20,0), pady=10)

    labelNombre = tk.Label(window, text="Nombre del producto:", font=("Arial", 23))
    labelNombre.grid(row=2, column=0, sticky="e", padx=(0,20), pady=10)
    input_nombre = tk.Entry(window, font=("Arial", 18), width=30)
    input_nombre.grid(row=2, column=1, sticky="w", padx=(20,0), pady=10)

    labelCategoria = tk.Label(window, text="Seleccione una categoría:", font=("Arial", 23))
    labelCategoria.grid(row=3, column=0, sticky="e", padx=(0,20), pady=10)
    input_categoria = ttk.Combobox(window, font=("Arial", 18), width=28, state="readonly")
    input_categoria["values"] = ("Tecnología", "Hogar", "Ropa", "Alimentos", "Otros")
    input_categoria.current(0)
    input_categoria.grid(row=3, column=1, sticky="w", padx=(20,0), pady=10)

    labelCantidad = tk.Label(window, text="Cantidad en existencia:", font=("Arial", 23))
    labelCantidad.grid(row=4, column=0, sticky="e", padx=(0,20), pady=10)
    input_Cantidad = tk.Entry(window, font=("Arial", 18), width=30)
    input_Cantidad.grid(row=4, column=1, sticky="w", padx=(20,0), pady=10)

    labelPrecio = tk.Label(window, text="Precio del producto:", font=("Arial", 23))
    labelPrecio.grid(row=5, column=0, sticky="e", padx=(0,20), pady=10)
    input_Precio = tk.Entry(window, font=("Arial", 18), width=30)
    input_Precio.grid(row=5, column=1, sticky="w", padx=(20,0), pady=10)

    def guardar():
        cod = input_codigo.get().strip()
        nom = input_nombre.get().strip()
        cat = input_categoria.get()
        cant_str = input_Cantidad.get().strip()
        prec_str = input_Precio.get().strip()

        if not (cod and nom and cat and cant_str and prec_str):
            messagebox.showerror("Error", "Todos los campos son obligatorios.", parent=window)
            return

        for producto in registro:
            if producto["codigo"] == cod:
                messagebox.showerror("Error", "Ese código ya existe.", parent=window)
                return

        try:
            cant = int(cant_str)
            prec = float(prec_str)
        except ValueError:
            messagebox.showerror("Error", "Cantidad y precio deben ser números.", parent=window)
            return

        if cant < 0 or prec < 0:
            messagebox.showerror("Error", "Cantidad y precio no pueden ser negativos.", parent=window)
            return

        registro.append({
            "codigo": cod,
            "nombre": nom,
            "categoria": cat,
            "cantidad": cant,
            "precio": prec
        })

        guardar_en_json()

        messagebox.showinfo("Éxito", "Producto registrado correctamente.", parent=window)

        input_codigo.delete(0, END)
        input_nombre.delete(0, END)
        input_Cantidad.delete(0, END)
        input_Precio.delete(0, END)
        input_categoria.current(0)

    
    btn_guardar = tk.Button(window, text="Guardar Producto", font=("Arial", 16), bg="green", fg="white", command=guardar)
    btn_guardar.grid(row=6, column=0, columnspan=3, pady=15, ipadx=30)

    
    btn_volver_menu = tk.Button(
        window, 
        text="🏠 Volver al Menú Principal", 
        font=("Arial", 14, "bold"), 
        bg="#555555", 
        fg="white", 
        command=lambda: volver_a_menu_principal(ventana_principal)
    )
    btn_volver_menu.grid(row=7, column=0, columnspan=3, pady=5, ipadx=20)

    
    btn_ver_lista = tk.Button(
        window, 
        text="Ver Registro Completo →", 
        font=("Arial", 14, "bold"), 
        bg="blue", 
        fg="white", 
        command=abrir_pantalla_tabla
    )
    btn_ver_lista.grid(row=8, column=0, columnspan=3, pady=15, ipadx=20)


def volver_a_menu_principal(ventana_principal):
    """Cierra las ventanas secundarias de registro y restaura la principal"""
    if 'ventana2' in globals() and ventana2.winfo_exists():
        ventana2.destroy()
    if 'window' in globals() and window.winfo_exists():
        window.destroy()
    ventana_principal.deiconify() 


def mostrar_pantalla_registro():
    """Muestra la pantalla de registro y oculta la de visualización"""
    if 'ventana2' in globals() and ventana2.winfo_exists():
        ventana2.withdraw()  
    window.deiconify()       

def abrir_pantalla_tabla():
    """Muestra la pantalla de la tabla y oculta la de registro"""
    global ventana2, contenedor_tabla
    
    window.withdraw() 
    
    if 'ventana2' in globals() and ventana2.winfo_exists():
        ventana2.deiconify()
        mostrar_lista() 
        return

    ventana2 = tk.Toplevel(window)
    ventana2.title("listo el registrar")
    ventana2.geometry("1366x768") 
    
    ventana2.protocol("WM_DELETE_WINDOW", mostrar_pantalla_registro)

    lbl_titulo = tk.Label(ventana2, text="REGISTRO DISPONIBLE", font=("Arial", 24, "bold"))
    lbl_titulo.pack(pady=15)

    btn_regresar = tk.Button(
        ventana2, 
        text="← Regresar al Registro", 
        bg="#555555", 
        fg="white", 
        font=("Arial", 12, "bold"), 
        command=mostrar_pantalla_registro
    )
    btn_regresar.pack(pady=5)

    contenedor_tabla = tk.Frame(ventana2)
    contenedor_tabla.pack(pady=20, padx=15, fill="x")

    mostrar_lista()

def mostrar_lista():
    for componente in contenedor_tabla.winfo_children():
        componente.destroy()
    
    if len(registro) == 0:
        lbl_vacio = tk.Label(contenedor_tabla, text="El registro está vacío. Registre un producto.", font=("Arial", 16))
        lbl_vacio.grid(row=0, column=0, columnspan=5, pady=20)
        return

    for i in range(5):
        contenedor_tabla.grid_columnconfigure(i, weight=1)

    titulos = ["Código", "Nombre", "Categoría", "Cantidad", "Precio"]
    anchos = [18, 25, 20, 15, 15] 
    
    for i in range(len(titulos)):
        celda_titulo = tk.Label(contenedor_tabla, text=titulos[i], font=("Arial", 14, "bold"), 
                                relief="solid", borderwidth=1, width=anchos[i], bg="#d3d3d3", pady=8)
        celda_titulo.grid(row=0, column=i, sticky="nsew")

    fila_actual = 1
    for p in registro:
        datos_producto = [p['codigo'], p['nombre'], p['categoria'], p['cantidad'], f"${p['precio']:.2f}"]
        
        for columna_actual in range(5):
            celda_dato = tk.Label(contenedor_tabla, text=datos_producto[columna_actual], font=("Arial", 14),
                                  relief="solid", borderwidth=1, width=anchos[columna_actual], bg="white", pady=8)
            celda_dato.grid(row=fila_actual, column=columna_actual, sticky="nsew")

        fila_actual += 1


if __name__ == "__main__":
    root_simulado = tk.Tk()
    root_simulado.title("Simulador de Menú Principal")
    root_simulado.geometry("400x200")
    
    lbl = tk.Label(root_simulado, text="Menú Principal (Simulado)", font=("Arial", 16))
    lbl.pack(pady=20)

    btn_ir = tk.Button(
        root_simulado, 
        text="➕ Ir a Registrar", 
        font=("Arial", 12, "bold"), 
        bg="green", 
        fg="white",
        command=lambda: abrir_pantalla_registro(root_simulado)
    )
    btn_ir.pack(pady=10)
    
    root_simulado.mainloop()