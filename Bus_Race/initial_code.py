'''
main.py

import os
import random
import time
from bus import Bus

def limpiar_consola():

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    bus_1 = Bus()
    bus_2 = Bus()
    print('CARRERA DE BUSES!!')
    print('AMARILLO vs ROJO')

    time.sleep(2)
    while True:
        limpiar_consola()
        Bus.dibujar_inicio_pista()
        bus_1.dibujar_bus(random.randint(1, 2), "AMARILLO")
        Bus.dibujar_inicio_pista()
        bus_1.dibujar_bus(random.randint(1, 2), "ROJO")
        Bus.dibujar_inicio_pista()

        if bus_1.posicion >= 100 or bus_2.posicion >= 100:
            if bus_1.posicion >= 100:
                print("GANA AMARILLO")
            else:
                print("GANA ROJO")
            time.sleep(10)
            break

        time.sleep(0.1)

main()

'''

'''
bus.py

class Bus:
    def __init__(self):
        self.posicion = 0

    @staticmethod
    def dibujar_inicio_pista():
        print("-------------------------------------------------------------------------------------------------------------------------")

    def dibujar_bus(self, desfase, nombre):
        self.posicion += desfase
        print("                                           ")
        print(" " * self.posicion + nombre)
        print(" " * self.posicion + "________________" )
        print(" " * self.posicion + "|__|__|__|__|__|__")
        print(" " * self.posicion + "|                 |")
        print(" " * self.posicion + "|----0---------0--|")

    @staticmethod
    def dibujar_final_pista():
        print("-------------------------------------------------------------------------------------------------------------------------")

'''
