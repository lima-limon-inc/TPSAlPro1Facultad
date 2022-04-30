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
    estado_del_juego = generar_tablero(NUMERO_FILA, NUMERO_COLU, CUANTO_MEZCLAR)

    matriz = estado_del_juego[0]
    vacio_fila = estado_del_juego[1]
    vacio_colu = estado_del_juego[2]
    historial_movimientos = estado_del_juego[3]
    movimientos_jugador = ""
    matriz_resuelta = generar_matriz(NUMERO_FILA, NUMERO_COLU)[0]

    while True: 
        mostrar_juego(matriz,historial_movimientos)
        movimientos_jugador = (input("Entrada:"))
        vacio_fila, vacio_colu, matriz, historial_movimientos = mover_vacio(movimientos_jugador, vacio_fila, vacio_colu, matriz, historial_movimientos)
        
        if matriz == matriz_resuelta:
            mostrar_juego(matriz, historial_movimientos)
            print("Ganaste! :)")
            break
        
        elif len(historial_movimientos) - CUANTO_MEZCLAR > CUANTO_MEZCLAR * 5:
            mostrar_juego(matriz, historial_movimientos)
            print("Perdiste! :(" + )
            break

main()
