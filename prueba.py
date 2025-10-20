# Principio S: separar responsabilidades

class ValidadorCliente:
    def validar(self, edad):
        if edad < 18:
            return False, "Debe ser mayor de edad"
        return True, None


class CalculadorDescuento:
    def calcular(self, edad):
        if edad > 60:
            return 0.2
        return 0.1


# Principio I y D: interfaz para notificaciones 

class Notificador:
    def notificar(self, mensaje):
        print(mensaje)


# Principios S, O y D: clase que orquesta el proceso sin mezclar tareas

class RegistroCliente:
    def __init__(self, validador, calculador, notificador):
        self.validador = validador
        self.calculador = calculador
        self.notificador = notificador

    def registrar(self, nombre, edad):
        valido, error = self.validador.validar(edad)
        if not valido:
            return error

        descuento = self.calculador.calcular(edad)
        self.notificador.notificar(
            f"Cliente {nombre} registrado con descuento de {descuento * 100}%"
        )
        return "Registro completo"


# Unificación de la función duplicada calcular_total 

class CalculadoraTotal:
    def calcular(self, precio, cantidad):
        return precio * cantidad  


# Refactorización de la clase Factura aplicando SRP e interfaces

class GuardarFactura:
    def guardar(self, factura):
        # lógica para guardar
        pass


class ImprimirFactura:
    def imprimir(self, factura):
        # lógica para imprimir
        pass


class EnviarFactura:
    def enviar(self, factura):
        # lógica para enviar por email
        pass


class Factura:
    def __init__(self, calculadora_total, guardar, imprimir, enviar):
        self.calculadora_total = calculadora_total
        self.guardar = guardar
        self.imprimir = imprimir
        self.enviar = enviar

    def procesar(self, precio, cantidad):
        total = self.calculadora_total.calcular(precio, cantidad)
        self.guardar.guardar(self)
        self.imprimir.imprimir(self)
        self.enviar.enviar(self)
        return total


# Uso de las clases 

validador = ValidadorCliente()
calculador = CalculadorDescuento()
notificador = Notificador()

registro = RegistroCliente(validador, calculador, notificador)
resultado = registro.registrar("Ana", 65)
print(resultado)

calculadora_total = CalculadoraTotal()
guardar = GuardarFactura()
imprimir = ImprimirFactura()
enviar = EnviarFactura()

factura = Factura(calculadora_total, guardar, imprimir, enviar)
total = factura.procesar(5000, 3)
print(f"Total calculado: {total}")
