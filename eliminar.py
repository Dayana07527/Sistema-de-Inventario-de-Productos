import tkinter as tk
from tkinter import messagebox
from backend_eliminar import buscar_producto, eliminar_producto

def crear_pantalla_eliminar(frame, productos):

    titulo = tk.Label(
        frame,
        text="Eliminar Producto",
        font=("Arial", 20, "bold"),
        bg="#F4F6F8"
    )
    titulo.pack(pady=20)

    tk.Label(frame, text="Código:", bg="#F4F6F8").pack()

    entrada_codigo = tk.Entry(frame)
    entrada_codigo.pack(pady=5)

    informacion = tk.Label(
        frame,
        text="",
        bg="#F4F6F8",
        justify="left"
    )
    informacion.pack(pady=20)

    producto_actual = {"producto": None}

    def buscar():

        codigo = entrada_codigo.get()

        producto = buscar_producto(productos, codigo)

        if producto:

            producto_actual["producto"] = producto

            informacion.config(
                text=f"Código: {producto['codigo']}\n"
                     f"Nombre: {producto['nombre']}\n"
                     f"Categoría: {producto['categoria']}\n"
                     f"Cantidad: {producto['cantidad']}\n"
                     f"Precio: ${producto['precio']}"
            )

        else:

            producto_actual["producto"] = None
            informacion.config(text="")
            messagebox.showerror(
                "Error",
                "Producto no encontrado."
            )

    def eliminar():

        if producto_actual["producto"] is None:

            messagebox.showwarning(
                "Aviso",
                "Primero busque un producto."
            )
            return

        respuesta = messagebox.askyesno(
            "Confirmar",
            "¿Desea eliminar este producto?"
        )

        if respuesta:

            eliminar_producto(
                productos,
                producto_actual["producto"]["codigo"]
            )

            informacion.config(text="")
            entrada_codigo.delete(0, tk.END)
            producto_actual["producto"] = None

            messagebox.showinfo(
                "Éxito",
                "Producto eliminado correctamente."
            )

    boton_buscar = tk.Button(
        frame,
        text="Buscar",
        command=buscar
    )
    boton_buscar.pack(pady=10)

    boton_eliminar = tk.Button(
        frame,
        text="Eliminar Producto",
        bg="red",
        fg="white",
        command=eliminar
    )
    boton_eliminar.pack(pady=10)