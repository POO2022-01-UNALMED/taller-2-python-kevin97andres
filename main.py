import random
class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, ncolor):
        print("¿Que color desea?")
        ncolor = input()
        if(ncolor == "rojo"):
            self.color = ncolor
        elif(ncolor == "verde"):
            self.color = ncolor
        elif(ncolor == "amarillo"):
            self.color = ncolor
        elif(ncolor == "vnegro"):
            self.color = ncolor
        elif(ncolor == "blanco"):
            self.color = ncolor
        else:
            print("Color no permitido")

class Auto:
    def __init__(self, modelo, precio, asientos, marca):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro