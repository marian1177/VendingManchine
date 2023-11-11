class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

class MaquinaExpendedora:
    def __init__(self):
        self.productos = {
            "Refresco": Producto("Refresco", 1.5, 10),
            "Snack": Producto("Snack", 2.0, 8),
            "Agua": Producto("Agua", 1.0, 15)
        }
        self.saldo_usuario = 0.0

    def mostrar_productos(self):
        return self.productos

    def agregar_saldo(self, monto):
        self.saldo_usuario += monto

    def realizar_compra(self, producto):
        if producto in self.productos and self.productos[producto].stock > 0:
            if self.saldo_usuario >= self.productos[producto].precio:
                self.saldo_usuario -= self.productos[producto].precio
                self.productos[producto].stock -= 1
                return f"¡Compra exitosa! Disfruta tu {producto}."
            else:
                return "Saldo insuficiente para realizar la compra."
        else:
            return "Producto no disponible."

# Ejemplo de Uso
maquina = MaquinaExpendedora()
print("Productos disponibles:", maquina.mostrar_productos())

maquina.agregar_saldo(5.0)
print("Saldo actual:", maquina.saldo_usuario)

resultado_compra = maquina.realizar_compra("Snack")
print(resultado_compra)
print("Stock de Snack:", maquina.productos["Snack"].stock)
print("Saldo restante:", maquina.saldo_usuario)
