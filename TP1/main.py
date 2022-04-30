# IMPORTS
from logica import *

# Funcion principal

def main():

   #list  ,    int    ,    int    ,    list       
    matriz, vacio_fila, vacio_colu, historial_movimientos = generar_tablero(NUMERO_FILA, NUMERO_COLU, CUANTO_MEZCLAR)
    movimientos_jugador = ""
    matriz_resuelta = generar_matriz(NUMERO_FILA, NUMERO_COLU)[0]

    while True: 
        mostrar_juego(matriz,historial_movimientos)
        movimientos_jugador = (input("Entrada:"))
        matriz, vacio_fila, vacio_colu, historial_movimientos = mover_vacio(movimientos_jugador, matriz, vacio_fila, vacio_colu, historial_movimientos)
        
        if matriz == matriz_resuelta:
            mostrar_juego(matriz, historial_movimientos)
            print("Ganaste! :)")
            break
        
        elif len(historial_movimientos) - CUANTO_MEZCLAR > CUANTO_MEZCLAR * 5:
            mostrar_juego(matriz, historial_movimientos)
            print("Perdiste! :(")
            print()
            print(frase_motivadora())
            print()
            print("$ python3 main.py para intentarlo de nuevo")
            break

main()
