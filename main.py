import tkinter as tk

#Ventana principal

root = tk.Tk()
root.title("ControlStock")
root.state("zoomed")
root.configure(bg="#F4F6F8")

#Encabezado

header = tk.Frame(root, bg="#0B3C6F", height=140)
header.pack(fill="x")

titulo = tk.Label(
    header,
    text="📦 ControlStock",
    bg="#0B3C6F",
    fg="white",
    font=("Segoe UI", 36, "bold")
)
titulo.pack(pady=(20, 5))

subtitulo = tk.Label(
    header,
    text="Sistema de Inventario de Productos",
    bg="#0B3C6F",
    fg="white",
    font=("Segoe UI", 16)
)
subtitulo.pack()

#Bienvenida

contenido = tk.Frame(root, bg="#F4F6F8")
contenido.pack(fill="both", expand=True)

bienvenida = tk.Label(
    contenido,
    text="Bienvenido al Sistema de Inventario",
    font=("Segoe UI", 30, "bold"),
    bg="#F4F6F8",
    fg="#23395B"
)
bienvenida.pack(pady=(45, 10))

texto = tk.Label(
    contenido,
    text="Seleccione una opción para continuar",
    font=("Segoe UI", 15),
    bg="#F4F6F8",
    fg="gray35"
)
texto.pack()

#Tarjetas

cards = tk.Frame(contenido, bg="#F4F6F8")
cards.pack(expand=True)

def crear_card(parent, icono, titulo, descripcion, color):

    frame = tk.Frame(
        parent,
        bg="white",
        width=240,
        height=360,
        highlightbackground="#D8D8D8",
        highlightthickness=1
    )
    frame.pack_propagate(False)

    icono_lbl = tk.Label(
        frame,
        text=icono,
        bg="white",
        font=("Segoe UI Emoji", 54)
    )
    icono_lbl.pack(pady=(25, 10))
    
    titulo_lbl = tk.Label(
        frame,
        text=titulo,
        bg="white",
        fg=color,
        font=("Segoe UI", 20, "bold")
    )
    titulo_lbl.pack(pady=(0, 10))

    descripcion_lbl = tk.Label(
        frame,
        text=descripcion,
        bg="white",
        fg="gray35",
        wraplength=190,
        justify="center",
        font=("Segoe UI", 12)
    )
    descripcion_lbl.pack(pady=(0, 15))

    boton = tk.Button(
        frame,
        text="Abrir",
        bg=color,
        fg="white",
        relief="flat",
        cursor="hand2",
        font=("Segoe UI", 13, "bold")
    )
    boton.pack(
        side="bottom",
        pady=(0, 25),
        ipadx=40,
        ipady=6
    )
    return frame

crear_card(
    cards,
    "➕",
    "Registrar",
    "Agregar un nuevo producto al inventario",
    "#27AE60"
).grid(row=0, column=0, padx=20)

crear_card(
    cards,
    "🔍",
    "Consultar",
    "Buscar productos registrados",
    "#2980B9"
).grid(row=0, column=1, padx=20)

crear_card(
    cards,
    "✏️",
    "Editar",
    "Modificar información de un producto",
    "#F39C12"
).grid(row=0, column=2, padx=20)

crear_card(
    cards,
    "🗑️",
    "Eliminar",
    "Eliminar un producto existente",
    "#E74C3C"
).grid(row=0, column=3, padx=20)

crear_card(
    cards,
    "📋",
    "Inventario",
    "Ver todos los productos",
    "#8E44AD"
).grid(row=0, column=4, padx=20)

#Pie de página

footer = tk.Frame(root, bg="white", height=50)
footer.pack(fill="x")

tk.Label(
    footer,
    text="© ControlStock 2026",
    bg="white",
    fg="gray50",
    font=("Segoe UI", 11)
).pack(side="left", padx=20)

root.mainloop()