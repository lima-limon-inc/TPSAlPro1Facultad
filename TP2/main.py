import gamelib
from logica import *


t = Tablero()
print(t.tablero_mutable[(t.pieza_seleccionada[0], t.pieza_seleccionada[1])].movimientos_validos)

def juego_nuevo(movimientos, n_nivel):
    '''inicializa el estado del juego para el numero de nivel dado'''
    return None

def juego_mostrar(juego):
    '''dibuja la interfaz de la aplicación en la ventana'''
    for fila in range(FILAS):
        pintar_blanco = (False if fila % 2 ==0 else True)

        for columna in range(COLUMNAS):
            pintar_blanco = not pintar_blanco
            color_celda = (COLOR_BLANCO if pintar_blanco else COLOR_NEGRO)

            gamelib.draw_rectangle(PIEZA_ANCHO * columna, PIEZA_LARGO * fila, PIEZA_ANCHO * columna + PIEZA_ANCHO, fila * PIEZA_LARGO + PIEZA_LARGO, fill=color_celda, width=4) # Funcion que se encarga de pintar los cuadraditos del tablero de ajedrez

            if (columna, fila) in t.tablero_mutable: #Si esto se cumple, significa que hay una pieza en el cuadrado que vamos a pintar

                gamelib.draw_image(t.tablero_mutable[(columna,fila)].devolver_imagen((True if (columna, fila) == t.pieza_seleccionada else False)), columna * 44, fila * 44)

                if (columna, fila) in t.tablero_mutable[t.pieza_seleccionada].movimientos_validos: # Si la pieza que va a dibujar se encuentra en algunas de los lugares donde la pieza seleccionada se puede mover, dibujamos un rectangulo rojo
                    gamelib.draw_rectangle(columna * 44 + 3, fila * 44 + 3, columna * 44 + 41, fila * 44 +41,fill = "" , outline="#db0404", width=2)

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
