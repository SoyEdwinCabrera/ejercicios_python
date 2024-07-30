import os
import random
import time
from bus import Bus  # Importa la clase Bus del archivo bus.py

def limpiar_consola():
    # Limpia la consola, diferente comando para Windows ('cls') y otros sistemas operativos ('clear')
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    bus_amarillo = Bus()  # Crea una instancia del bus amarillo
    bus_rojo = Bus()      # Crea una instancia del bus rojo
    print('CARRERA DE BUSES!!')
    print('AMARILLO vs ROJO')

    time.sleep(2)  # Espera 2 segundos antes de iniciar la carrera

    while True:
        limpiar_consola()  # Limpia la consola en cada iteración del ciclo
        Bus.dibujar_inicio_pista()  # Dibuja la línea de inicio de la pista
        bus_amarillo.dibujar_bus("AMARILLO")  # Dibuja el bus amarillo en su posición actual
        Bus.dibujar_inicio_pista()  # Dibuja la línea de inicio de la pista nuevamente
        bus_rojo.dibujar_bus("ROJO")  # Dibuja el bus rojo en su posición actual
        Bus.dibujar_inicio_pista()  # Dibuja la línea de inicio de la pista nuevamente

        bus_amarillo.mover()  # Mueve el bus amarillo
        bus_rojo.mover()      # Mueve el bus rojo

        # Verifica si algún bus ha alcanzado o superado la posición 100
        if bus_amarillo.posicion >= 100 or bus_rojo.posicion >= 100:
            if bus_amarillo.posicion >= 100:
                print("GANA AMARILLO")  # Anuncia que el bus amarillo ha ganado
            else:
                print("GANA ROJO")      # Anuncia que el bus rojo ha ganado
            time.sleep(3)  # Espera 3 segundos antes de terminar el programa
            break

        time.sleep(0.1)  # Espera 0.1 segundos antes de la siguiente iteración del ciclo

if __name__ == "__main__":
    main()  # Ejecuta la función main si este archivo es el programa principal
