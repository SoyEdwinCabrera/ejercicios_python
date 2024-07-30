import random

class Bus:
    def __init__(self):
        # Inicializa la posición del bus en 0
        self.posicion = 0

    def mover(self):
        # Incrementa la posición del bus de forma aleatoria entre 1 y 2
        self.posicion += random.randint(1, 2)

    @staticmethod
    def dibujar_inicio_pista():
        # Dibuja la línea de inicio de la pista
        print("=" * 120)

    def dibujar_bus(self, color):
        # Dibuja el bus en su posición actual, con su color
        print(" " * self.posicion + f"BUS {color}")
        print(" " * self.posicion + "________________" )
        print(" " * self.posicion + "|__|__|__|__|__|__")
        print(" " * self.posicion + "|                 |")
        print(" " * self.posicion + "|----0---------0--|")
