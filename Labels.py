import tkinter as tk

class MaquinaExpendedora:
    def __init__(self, root):
        self.root = root
        self.root.title("Máquina Expendedora")

        # Etiqueta para mostrar el saldo
        self.saldo_label = tk.Label(root, text="Saldo: $0.00")
        self.saldo_label.pack()

        # Etiqueta para mostrar la selección actual
        self.seleccion_label = tk.Label(root, text="Selección actual: Ninguna")
        self.seleccion_label.pack()

        # Botones de selección
        self.boton_seleccion1 = tk.Button(root, text="Producto 1", command=lambda: self.seleccionar_producto(1))
        self.boton_seleccion1.pack()

        self.boton_seleccion2 = tk.Button(root, text="Producto 2", command=lambda: self.seleccionar_producto(2))
        self.boton_seleccion2.pack()

        # Botón para agregar saldo
        self.boton_agregar_saldo = tk.Button(root, text="Agregar Saldo", command=self.agregar_saldo)
        self.boton_agregar_saldo.pack()

    def seleccionar_producto(self, numero_producto):
        # Lógica para la selección de productos
        self.seleccion_label.config(text=f"Selección actual: Producto {numero_producto}")

    def agregar_saldo(self):
        # Lógica para agregar saldo
        # Actualizar la etiqueta del saldo
        self.saldo_label.config(text="Saldo: $10.00")

if __name__ == "__main__":
    root = tk.Tk()
    maquina = MaquinaExpendedora(root)
    root.mainloop()
