import gamelib
from logica import *

def juego_nuevo(movimientos, n_nivel):
    '''inicializa el estado del juego para el numero de nivel dado'''
    return None

def juego_mostrar(juego):
    '''dibuja la interfaz de la aplicación en la ventana'''
    for fila in range(FILAS):
        pintar_blanco = (True if fila % 2 ==0 else False)

        for columna in range(COLUMNAS):
            color = (COLOR_BLANCO if pintar_blanco else COLOR_NEGRO)

            gamelib.draw_rectangle(PIEZA_ANCHO * columna, PIEZA_LARGO * fila, PIEZA_ANCHO * columna + PIEZA_ANCHO, fila * PIEZA_LARGO + PIEZA_LARGO, fill=color, width=4)
            gamelib.draw_image("sprites/torre_rojo.gif", 0,0)




            pintar_blanco = not pintar_blanco
    gamelib.draw_end()

def main():
    gamelib.title("Shape Shifter Chess")
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)

    juego = juego_nuevo(3,3)

    while gamelib.is_alive():
        juego_mostrar(juego)

        ev = gamelib.wait()
        if not ev:
            break

        if ev.type == gamelib.EventType.ButtonPress and ev.mouse_button == 1:
            print(f'se ha presionado el botón del mouse: {ev.x} {ev.y}')
        elif ev.type == gamelib.EventType.KeyPress:
            print(f'se ha presionado la tecla: {ev.key}')

gamelib.init(main)

