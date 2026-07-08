from tkinter import messagebox

def buscar_producto(productos, codigo):
    for producto in productos:
        if producto["codigo"] == codigo:
            return producto
    return None


def eliminar_producto(productos, codigo):
    for producto in productos:
        if producto["codigo"] == codigo:
            productos.remove(producto)
            return True
    return False