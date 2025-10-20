# clientes.py (malo — mezcla responsabilidades)
def registrar_cliente(nombre, edad):
    # validar
    if edad < 18:
        return "Debe ser mayor de edad"

    # calcular descuento
    if edad > 60:
        descuento = 0.2
    else:
        descuento = 0.1

    # mostrar mensaje (interfaz)
    print(f"Cliente {nombre} registrado con descuento de {descuento*100}%")
    return "Registro completo"


# archivo 1
def calcular_total(precio, cantidad):
    return precio * cantidad

# archivo 2
def calcular_total(precio, cantidad):
    return (precio * cantidad) + 100  # versión diferente


class Factura:
    def calcular_total(self): ...
    def guardar_factura(self): ...
    def imprimir_factura(self): ...
    def enviar_por_email(self): ...
