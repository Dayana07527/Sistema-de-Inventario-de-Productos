import json
import tkinter as tk
from tkinter import ttk


# ---------------------------------------------------------
# CARGA DE DATOS (Lee el JSON para estar sincronizado)
# ---------------------------------------------------------
def cargar_productos():
  try:
    with open("inventario.json", "r", encoding="utf-8") as f:
      lista = json.load(f)
      # Convertimos la lista del JSON a un diccionario por código
      return {item["codigo"]: item for item in lista}
  except FileNotFoundError:
    return {}


# ---------------------------------------------------------
# FUNCIÓN/PANTALLA DE CONSULTA
# ---------------------------------------------------------
def crear_pantalla_consultar(parent, comando_volver=None):
  productos = cargar_productos()

  # Contenedor principal de la vista
  frame_consultar = tk.Frame(parent, bg="#F4F6F8")

  # --- ENCABEZADO ---
  header = tk.Frame(frame_consultar, bg="#0B3C6F", height=120)
  header.pack(fill="x")
  header.pack_propagate(False)

  # Botón Volver posicionado sobre el Header
  if comando_volver:
    btn_volver = tk.Button(
        header,
        text="← Volver al Menú",
        command=comando_volver,
        font=("Segoe UI", 11, "bold"),
        bg="#0B3C6F",
        fg="white",
        activebackground="#082A4D",
        activeforeground="white",
        bd=0,
        cursor="hand2",
    )
    btn_volver.pack(anchor="w", padx=20, pady=15)

  titulo_header = tk.Label(
      header,
      text="🔍 Consultar Producto",
      bg="#0B3C6F",
      fg="white",
      font=("Segoe UI", 26, "bold"),
  )
  titulo_header.pack(pady=(0, 10))

  # --- CONTENIDO PRINCIPAL (TARJETA CENTRADA) ---
  contenido = tk.Frame(frame_consultar, bg="#F4F6F8")
  contenido.pack(fill="both", expand=True)

  # Tarjeta de Búsqueda
  card = tk.Frame(
      contenido,
      bg="white",
      width=550,
      height=460,
      highlightbackground="#D8D8D8",
      highlightthickness=1,
  )
  card.pack(pady=40)
  card.pack_propagate(False)

  tk.Label(
      card,
      text="Búsqueda por Código",
      bg="white",
      fg="#23395B",
      font=("Segoe UI", 18, "bold"),
  ).pack(pady=(25, 5))

  tk.Label(
      card,
      text="Ingrese el código del producto (ej: PRF-001, BEB-002)",
      bg="white",
      fg="gray45",
      font=("Segoe UI", 11),
  ).pack(pady=(0, 15))

  # Área del campo de texto
  frame_input = tk.Frame(card, bg="white")
  frame_input.pack(pady=5)

  entrada_codigo = tk.Entry(
      frame_input,
      font=("Segoe UI", 14),
      width=18,
      justify="center",
      bd=2,
      relief="groove",
  )
  entrada_codigo.pack(side="left", padx=5)
  entrada_codigo.focus()

  # Frame para la tarjeta de resultado (Inicialmente limpia)
  res_card = tk.Frame(card, bg="#F4F6F8", bd=1, relief="solid")
  lbl_res_nombre = tk.Label(
      res_card,
      text="",
      font=("Segoe UI", 15, "bold"),
      bg="#F4F6F8",
      fg="#23395B",
  )
  lbl_res_categoria = tk.Label(
      res_card, text="", font=("Segoe UI", 11), bg="#F4F6F8", fg="gray40"
  )
  lbl_res_detalles = tk.Label(
      res_card, text="", font=("Segoe UI", 13), bg="#F4F6F8", fg="#27AE60"
  )

  def ejecutar_busqueda(event=None):
    codigo = entrada_codigo.get().strip().upper()

    # Ocultar resultado anterior
    res_card.pack_forget()

    if not codigo:
      lbl_res_nombre.config(text="⚠️ Código Vacío", fg="#E74C3C")
      lbl_res_categoria.config(
          text="Por favor ingrese un código para buscar."
      )
      lbl_res_detalles.config(text="")
      res_card.pack(fill="x", padx=40, pady=20)
      return

    if codigo in productos:
      prod = productos[codigo]
      lbl_res_nombre.config(text=f"📦 {prod['nombre']}", fg="#23395B")
      lbl_res_categoria.config(
          text=f"Categoría: {prod.get('categoria', 'N/A')}"
      )
      lbl_res_detalles.config(
          text=f"Precio: ${prod['precio']:.2f}   |   Stock: {prod.get('cantidad', prod.get('stock', 0))} uds.",
          fg="#27AE60",
      )
      res_card.pack(fill="x", padx=40, pady=20)
    else:
      lbl_res_nombre.config(
          text="❌ Producto No Encontrado", fg="#E74C3C"
      )
      lbl_res_categoria.config(
          text="El código ingresado no existe en el inventario."
      )
      lbl_res_detalles.config(text="")
      res_card.pack(fill="x", padx=40, pady=20)

  # Empacar labels de resultados dentro del card flotante
  lbl_res_nombre.pack(pady=(12, 2))
  lbl_res_categoria.pack(pady=2)
  lbl_res_detalles.pack(pady=(2, 12))

  # Permite buscar al presionar 'Enter'
  entrada_codigo.bind("<Return>", ejecutar_busqueda)

  # Botón de Búsqueda Azul
  btn_buscar = tk.Button(
      card,
      text="🔍 Buscar",
      bg="#2980B9",
      fg="white",
      activebackground="#1F618D",
      activeforeground="white",
      font=("Segoe UI", 12, "bold"),
      relief="flat",
      cursor="hand2",
      command=ejecutar_busqueda,
  )
  btn_buscar.pack(pady=15, ipadx=30, ipady=4)

  return frame_consultar


# ---------------------------------------------------------
# MODO INDEPENDIENTE (Para probar solo este archivo)
# ---------------------------------------------------------
if __name__ == "__main__":
  root = tk.Tk()
  root.title("ControlStock - Consultar")
  root.state("zoomed")
  root.configure(bg="#F4F6F8")

  pantalla = crear_pantalla_consultar(root, comando_volver=root.destroy)
  pantalla.pack(fill="both", expand=True)

  root.mainloop()