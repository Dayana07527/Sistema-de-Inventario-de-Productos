import tkinter as tk
from tkinter import ttk
import json
import os

def crear_pantalla_editar(ventana):
    frame = tk.Frame(ventana)
    return frame

# -------- NOMBRE DEL ARCHIVO JSON --------
ARCHIVO_DATOS = "inventario.json"

# -------- DATOS POR DEFECTO --------
productos_por_defecto = [
    {"nombre": "Manzanas", "categoria": "Frutas", "cantidad": 30, "precio": 3.50},
    {"nombre": "Bananos", "categoria": "Frutas", "cantidad": 30, "precio": 3.50},
    {"nombre": "Naranjas", "categoria": "Frutas", "cantidad": 30, "precio": 3.50},
    {"nombre": "Lechuga", "categoria": "Verduras", "cantidad": 25, "precio": 2.00},
    {"nombre": "Tomate", "categoria": "Verduras", "cantidad": 25, "precio": 2.00},
    {"nombre": "Zanahoria", "categoria": "Verduras", "cantidad": 25, "precio": 2.00},
    {"nombre": "Carne de res", "categoria": "Carnes", "cantidad": 15, "precio": 9.50},
    {"nombre": "Pollo", "categoria": "Carnes", "cantidad": 15, "precio": 9.50},
    {"nombre": "Pescado", "categoria": "Carnes", "cantidad": 15, "precio": 9.50},
    {"nombre": "Huevos", "categoria": "Lácteos y Huevos", "cantidad": 40, "precio": 4.00},
    {"nombre": "Quesos y embutidos", "categoria": "Lácteos y Huevos", "cantidad": 20, "precio": 6.50},
    {"nombre": "Agua", "categoria": "Bebidas", "cantidad": 50, "precio": 0.75},
    {"nombre": "Jugos", "categoria": "Bebidas", "cantidad": 30, "precio": 1.50},
    {"nombre": "Refrescos", "categoria": "Bebidas", "cantidad": 35, "precio": 1.25},
    {"nombre": "Cafe", "categoria": "Bebidas", "cantidad": 25, "precio": 5.00},
    {"nombre": "Te", "categoria": "Bebidas", "cantidad": 20, "precio": 2.50},
    {"nombre": "Leche", "categoria": "Bebidas", "cantidad": 30, "precio": 1.75},
    {"nombre": "Bebidas energeticas", "categoria": "Bebidas", "cantidad": 18, "precio": 2.75},
    {"nombre": "Shampoo", "categoria": "Cuidado personal", "cantidad": 15, "precio": 4.50},
    {"nombre": "Jabon", "categoria": "Cuidado personal", "cantidad": 12, "precio": 1.25},
    {"nombre": "Pasta dental", "categoria": "Cuidado personal", "cantidad": 20, "precio": 2.75},
    {"nombre": "Cepillo de dientes", "categoria": "Cuidado personal", "cantidad": 20, "precio": 2.25},
    {"nombre": "Desodorante", "categoria": "Cuidado personal", "cantidad": 18, "precio": 3.50},
    {"nombre": "Papel higiénico", "categoria": "Cuidado personal", "cantidad": 40, "precio": 5.50},
    {"nombre": "Protector solar", "categoria": "Cuidado personal", "cantidad": 10, "precio": 7.00},
    {"nombre": "Detergente", "categoria": "Cuidado del hogar", "cantidad": 15, "precio": 5.50},
    {"nombre": "Suavizante de ropa", "categoria": "Cuidado del hogar", "cantidad": 12, "precio": 5.00},
    {"nombre": "Cloro", "categoria": "Cuidado del hogar", "cantidad": 20, "precio": 2.50},
    {"nombre": "Desinfectante", "categoria": "Cuidado del hogar", "cantidad": 15, "precio": 3.50},
    {"nombre": "Bolsas de basura", "categoria": "Cuidado del hogar", "cantidad": 25, "precio": 3.00},
    {"nombre": "Esponjas", "categoria": "Cuidado del hogar", "cantidad": 20, "precio": 1.75},
    {"nombre": "Limpiadores multiusos", "categoria": "Cuidado del hogar", "cantidad": 10, "precio": 4.50},
    {"nombre": "Pañales", "categoria": "Cuidado del bebé", "cantidad": 15, "precio": 13.00},
    {"nombre": "Toallitas húmedas", "categoria": "Cuidado del bebé", "cantidad": 20, "precio": 5.00},
    {"nombre": "Fórmula infantil", "categoria": "Cuidado del bebé", "cantidad": 10, "precio": 20.00},
    {"nombre": "Talco", "categoria": "Cuidado del bebé", "cantidad": 12, "precio": 3.50},
    {"nombre": "Shampoo para bebé", "categoria": "Cuidado del bebé", "cantidad": 10, "precio": 5.50},
    {"nombre": "Biberones", "categoria": "Cuidado del bebé", "cantidad": 15, "precio": 7.00},
    {"nombre": "Alimento para perros y gatos", "categoria": "Cuidado de mascotas", "cantidad": 15, "precio": 9.00},
    {"nombre": "Premios para mascotas", "categoria": "Cuidado de mascotas", "cantidad": 20, "precio": 3.50},
    {"nombre": "Arena para gatos", "categoria": "Cuidado de mascotas", "cantidad": 10, "precio": 8.00},
    {"nombre": "Shampoo para mascotas", "categoria": "Cuidado de mascotas", "cantidad": 10, "precio": 5.50},
    {"nombre": "Juguetes", "categoria": "Cuidado de mascotas", "cantidad": 12, "precio": 4.50},
    {"nombre": "Correas", "categoria": "Cuidado de mascotas", "cantidad": 10, "precio": 7.00}
]

# -------- FUNCIONES DE PERSISTENCIA (JSON) --------
def cargar_datos():
    if os.path.exists(ARCHIVO_DATOS):
        try:
            with open(ARCHIVO_DATOS, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return productos_por_defecto
    else:
        guardar_datos(productos_por_defecto)
        return productos_por_defecto

def guardar_datos(datos):
    try:
        with open(ARCHIVO_DATOS, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error al guardar el archivo JSON: {e}")

productos = cargar_datos()

# -------- PALETA DE COLORES --------
bg_principal = "#F4F6F9"        
azul_header = "#0D3E74"         
blanco_tarjeta = "#FFFFFF"      
borde_tarjeta = "#E2E8F0"      

color_azul_btn = "#1F78B4"      
color_naranja_btn = "#FF9F00"   

producto_a_editar = ""

# -------- LÓGICA DE NAVEGACIÓN Y ACTUALIZACIÓN --------
def actualizar_comboboxes():
    nombres_actualizados = [p["nombre"] for p in productos]
    categorias_actualizadas = sorted(set(p["categoria"] for p in productos if "categoria" in p))
    cantidades_actualizadas = sorted(set(str(p["cantidad"]) for p in productos), key=int)
    precios_actualizadas = sorted(set(str(p["precio"]) for p in productos), key=float)
    
    combo_producto.config(values=nombres_actualizados)
    combo_categoria.config(values=categorias_actualizadas)
    combo_cantidad.config(values=cantidades_actualizadas)
    combo_precio.config(values=precios_actualizadas)
    
    if nombres_actualizados: combo_producto.current(0)
    if categorias_actualizadas: combo_categoria.current(0)
    if cantidades_actualizadas: combo_cantidad.current(0)
    if precios_actualizadas: combo_precio.current(0)

def ir_a_pantalla_2():
    global producto_a_editar
    producto_a_editar = combo_producto.get()
    
    frame_pantalla1.pack_forget()
    frame_pantalla2.pack(fill="both", expand=True, pady=5)
    
    entry_nuevo_nombre.delete(0, tk.END)
    entry_nueva_categoria.delete(0, tk.END)
    entry_nueva_cantidad.delete(0, tk.END)
    entry_nuevo_precio.delete(0, tk.END)
    
    entry_nuevo_nombre.insert(0, producto_a_editar)
    entry_nueva_categoria.insert(0, combo_categoria.get())
    entry_nueva_cantidad.insert(0, combo_cantidad.get())
    entry_nuevo_precio.insert(0, combo_precio.get())

def regresar_a_pantalla1():
    frame_pantalla2.pack_forget()
    frame_pantalla1.pack(fill="both", expand=True, pady=10)
    resultado.config(text="") 

def cerrar_ventana():
    """Función para el botón volver de la pantalla principal"""
    screen.destroy()

def guardar_cambios():
    nombre_nuevo = entry_nuevo_nombre.get()
    categoria_nueva = entry_nueva_categoria.get()
    
    try:
        cantidad_nueva = int(entry_nueva_cantidad.get())
        precio_nuevo = float(entry_nuevo_precio.get())
    except ValueError:
        resultado.config(text="❌ Error: Cantidad debe ser entero y Precio un número.", fg="#D32F2F")
        return
 
    for producto in productos:
        if producto["nombre"] == producto_a_editar:
            producto["nombre"] = nombre_nuevo
            producto["categoria"] = categoria_nueva
            producto["cantidad"] = cantidad_nueva
            producto["precio"] = precio_nuevo
            
            guardar_datos(productos)
            actualizar_comboboxes()
 
            resultado.config(text=f"✅ Producto '{nombre_nuevo}' actualizado y guardado con éxito.", fg="#2E7D32")
            
            frame_pantalla2.pack_forget()
            frame_pantalla1.pack(fill="both", expand=True, pady=10)
            return

# -------- VENTANA PRINCIPAL --------
screen = tk.Tk()
screen.title("ControlStock - Sistema de Inventario")
screen.state("zoomed")
screen.configure(bg=bg_principal)

style = ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground="white", background="#E2E8F0", font=("Segoe UI", 12))

# ==========================================
# HEADER (BARRA SUPERIOR AZUL)
# ==========================================
header = tk.Frame(screen, bg=azul_header, height=100)
header.pack(fill="x", side="top")
header.pack_propagate(False)

tk.Label(
    header, text="📦 ControlStock", 
    bg=azul_header, fg="white", font=("Segoe UI", 24, "bold")
).pack(pady=(10, 0))

tk.Label(
    header, text="Sistema de Inventario de Productos", 
    bg=azul_header, fg="#A0C4DF", font=("Segoe UI", 11)
).pack()


# ==========================================
# PANTALLA 1: SELECCIONAR TODO
# ==========================================
frame_pantalla1 = tk.Frame(screen, bg=bg_principal)
frame_pantalla1.pack(fill="both", expand=True, pady=10)

tarjeta_p1 = tk.Frame(frame_pantalla1, bg=blanco_tarjeta, bd=1, highlightbackground=borde_tarjeta, highlightthickness=1)
tarjeta_p1.pack(pady=10, padx=20, ipady=15)

tk.Label(tarjeta_p1, text="Editar Producto", bg=blanco_tarjeta, fg=color_azul_btn, font=("Segoe UI", 18, "bold")).pack(pady=10)

tk.Label(tarjeta_p1, text="Elige el producto que deseas editar:", bg=blanco_tarjeta, fg="#334155", font=("Segoe UI", 12, "bold")).pack(anchor="w", padx=60, pady=(4, 2))
nombres = [p["nombre"] for p in productos]
combo_producto = ttk.Combobox(tarjeta_p1, values=nombres, state="readonly", width=50)
combo_producto.pack(pady=(0, 8), padx=60, ipady=4)

tk.Label(tarjeta_p1, text="Elige la categoría que deseas editar:", bg=blanco_tarjeta, fg="#334155", font=("Segoe UI", 12, "bold")).pack(anchor="w", padx=60, pady=(4, 2))
categorias = sorted(set(p["categoria"] for p in productos if "categoria" in p))
combo_categoria = ttk.Combobox(tarjeta_p1, values=categorias, state="readonly", width=50)
combo_categoria.pack(pady=(0, 8), padx=60, ipady=4)

tk.Label(tarjeta_p1, text="Elige la cantidad que deseas editar:", bg=blanco_tarjeta, fg="#334155", font=("Segoe UI", 12, "bold")).pack(anchor="w", padx=60, pady=(4, 2))
cantidades = sorted(set(str(p["cantidad"]) for p in productos), key=int)
combo_cantidad = ttk.Combobox(tarjeta_p1, values=cantidades, state="readonly", width=50)
combo_cantidad.pack(pady=(0, 8), padx=60, ipady=4)

tk.Label(tarjeta_p1, text="Elige el precio que deseas editar:", bg=blanco_tarjeta, fg="#334155", font=("Segoe UI", 12, "bold")).pack(anchor="w", padx=60, pady=(4, 2))
precios = sorted(set(str(p["precio"]) for p in productos), key=float)
combo_precio = ttk.Combobox(tarjeta_p1, values=precios, state="readonly", width=50)
combo_precio.pack(pady=(0, 15), padx=60, ipady=4)

if nombres: combo_producto.current(0)
if categorias: combo_categoria.current(0)
if cantidades: combo_cantidad.current(0)
if precios: combo_precio.current(0)

btn_seleccionar = tk.Button(
    tarjeta_p1, text="Seleccionar todo", command=ir_a_pantalla_2,
    bg=color_azul_btn, fg="white", font=("Segoe UI", 13, "bold"), 
    activebackground="#1A6396", activeforeground="white", bd=0, cursor="hand2"
)
btn_seleccionar.pack(fill="x", padx=60, ipady=8)

# --- TU BOTÓN VOLVER AGREGADO A LA PANTALLA 1 ---
boton_volver_p1 = tk.Button(
    tarjeta_p1,
    text="← Volver",
    command=cerrar_ventana,
    font=("Arial", 11, "bold"),
    bg=blanco_tarjeta,
    fg="#64748B",
    activebackground=blanco_tarjeta,
    activeforeground=color_azul_btn,
    bd=0,
    cursor="hand2"
)
boton_volver_p1.pack(anchor="w", padx=13, pady=8)
boton_volver_p1.pack(pady=14)


# ==========================================
# PANTALLA 2: NUEVOS DATOS
# ==========================================
frame_pantalla2 = tk.Frame(screen, bg=bg_principal)

tarjeta_p2 = tk.Frame(frame_pantalla2, bg=blanco_tarjeta, bd=1, highlightbackground=borde_tarjeta, highlightthickness=1)
tarjeta_p2.pack(pady=10, padx=20, ipady=15)

# --- BOTÓN VOLVER (PANTALLA 2) ---
boton_volver_p2 = tk.Button(
    tarjeta_p2, 
    text="← Volver", 
    command=regresar_a_pantalla1, 
    font=("Segoe UI", 11, "bold"),
    bg=blanco_tarjeta,
    fg=color_azul_btn,
    activebackground=blanco_tarjeta,
    activeforeground="#1A6396",
    bd=0, 
    cursor="hand2"   
)
boton_volver_p2.pack(anchor="w", padx=60, pady=(10, 0))

tk.Label(tarjeta_p2, text="Modificar Valores", bg=blanco_tarjeta, fg=color_naranja_btn, font=("Segoe UI", 18, "bold")).pack(pady=10)

tk.Label(tarjeta_p2, text="Coloca el nombre nuevo:", bg=blanco_tarjeta, fg="#334155", font=("Segoe UI", 12, "bold")).pack(anchor="w", padx=60, pady=(4, 2))
entry_nuevo_nombre = tk.Entry(tarjeta_p2, font=("Segoe UI", 12), bd=1, relief="solid", highlightthickness=1, highlightbackground=borde_tarjeta)
entry_nuevo_nombre.pack(fill="x", padx=60, pady=(0, 8), ipady=4)

tk.Label(tarjeta_p2, text="Coloca la nueva categoría:", bg=blanco_tarjeta, fg="#334155", font=("Segoe UI", 12, "bold")).pack(anchor="w", padx=60, pady=(4, 2))
entry_nueva_categoria = tk.Entry(tarjeta_p2, font=("Segoe UI", 12), bd=1, relief="solid", highlightthickness=1, highlightbackground=borde_tarjeta)
entry_nueva_categoria.pack(fill="x", padx=60, pady=(0, 8), ipady=4)

tk.Label(tarjeta_p2, text="Coloca la nueva cantidad:", bg=blanco_tarjeta, fg="#334155", font=("Segoe UI", 12, "bold")).pack(anchor="w", padx=60, pady=(4, 2))
entry_nueva_cantidad = tk.Entry(tarjeta_p2, font=("Segoe UI", 12), bd=1, relief="solid", highlightthickness=1, highlightbackground=borde_tarjeta)
entry_nueva_cantidad.pack(fill="x", padx=60, pady=(0, 8), ipady=4)

tk.Label(tarjeta_p2, text="Coloca el nuevo precio:", bg=blanco_tarjeta, fg="#334155", font=("Segoe UI", 12, "bold")).pack(anchor="w", padx=60, pady=(4, 2))
entry_nuevo_precio = tk.Entry(tarjeta_p2, font=("Segoe UI", 12), bd=1, relief="solid", highlightthickness=1, highlightbackground=borde_tarjeta)
entry_nuevo_precio.pack(fill="x", padx=60, pady=(0, 15), ipady=4)

btn_guardar = tk.Button(
    tarjeta_p2, text="Guardar Cambios", command=guardar_cambios,
    bg=color_naranja_btn, fg="white", font=("Segoe UI", 13, "bold"), 
    activebackground="#E08B00", activeforeground="white", bd=0, cursor="hand2"
)
btn_guardar.pack(fill="x", padx=60, ipady=8)


# -------- MENSAJE DE RESULTADO --------
resultado = tk.Label(
    screen, text="", bg=bg_principal, font=("Segoe UI", 12, "bold")
)
resultado.pack(side="bottom", pady=10)
 
screen.mainloop()