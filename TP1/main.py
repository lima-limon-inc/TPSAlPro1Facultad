# IMPORTS
from logica import *


# Funcion principal

def main():
    '''
    1er elemento: Matriz del juego en su estado actual. Tipo: Lista de listas
    2do elemento: Coordenada del espacio vacio. Tipo lista
    3er elemento: CANTIDAD de movimientos del jugador. Tipo: Integer
    4to elemento: Movimientos del jugador. Tipo: String
    '''
    estado_del_juego = [generar_matriz(),[ULTIMA_FILA, ULTIMA_COLU], [], ""] 

    matriz = estado_del_juego[0]
    coord_vacio = estado_del_juego[1]
    historial_movimientos = estado_del_juego[2]
    movimientos_jugador = estado_del_juego[3]

    while True: 
        mostrar_juego(matriz,historial_movimientos)
        print(f"DEBUG MOVIMIENTOS INPUT: {movimientos_jugador}")
        movimientos_jugador += (input("Entrada:"))
        movimientos_jugador, coord_vacio, matriz, historial_movimientos = mover_vacio(movimientos_jugador, coord_vacio, matriz, historial_movimientos)

main()
