# Imports
import gamelib

# Constantes
## Constantes globales relacionadas con la ventana
ANCHO_VENTANA = 300
ALTO_VENTANA = 300

## Constantes relacionadas con el tablero
FILAS = 10
COLUMNAS = 10
CUADRADO_ANCHO = ANCHO_VENTANA * 0.1
CUADRADO_ALTO = ALTO_VENTANA * 0.1


def juego_crear():
    '''Funcion que se ejecuta al iniciar el juegop. Esta devuelve dos cosas un string indicando el turno de quien es y una matriz que contiene el estado de todas las casillas del juego, cada casilla puede tener 1 de 3 valores: 1) "X": significa que el jugador "X" selecciono la casilla. 2) "O": Significa que el jugador "O" selecciono la casilla. 3) "": Significa que la casilla no fue seleccionada
    Recibe:
        Nada
    Devuelve:
        0. juego -> list. Matriz de filas X columnas
        1. quien_juega -> str. String que representa a que jugador le toca jugar (ejemplo: "X" indica que es el turno del jugador "X")
        '''
    juego = []
    for fila in range(FILAS):
        juego.append([])
        for columna in range(COLUMNAS):
            juego[fila].append("")
    
    quien_juega = "X"
    return juego, quien_juega

def juego_actualizar(juego, x, y,quien_juega):
    '''
    Funcion que se encarga de actualizar los datos de la matriz y cambiar a quien le toca jugar; basandose en donde el usuario hizo click.
    Recibe:
        0. juego -> list. Matriz de filas
        1. x -> int. Coordenadas x del mouse donde el usuario hizo click
        2. y -> int. Coordenadas y del mouse donde el usuario hizo click
        3. quien_juega -> str. String que representa a que jugador le toca jugar (ejemplo: "X" indica que es el turno del jugador "X")
    Devuelve:
        0. juego -> list. Matriz de filas
        1. quien_juega -> str. String que representa a que jugador le toca jugar (ejemplo: "X" indica que es el turno del jugador "X")
    '''

    for columna in range(COLUMNAS):
        if not (columna * CUADRADO_ANCHO <= x <= columna * CUADRADO_ANCHO + CUADRADO_ANCHO):
            continue
        x = columna
        for fila in range(FILAS):
            if not (fila * CUADRADO_ALTO <= y <= fila * CUADRADO_ALTO + CUADRADO_ALTO):
                continue
            y = fila

    if juego[y][x] == "":
        juego[y][x] = quien_juega
        quien_juega = ("O" if quien_juega == "X" else "X")

    return juego, quien_juega

def juego_mostrar(juego, quien_juega):
    '''Funcion que se encarga de mostrar la interfaz grafica del juego. '''
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            gamelib.draw_rectangle(CUADRADO_ANCHO * columna, CUADRADO_ALTO * fila, CUADRADO_ANCHO * columna + CUADRADO_ANCHO, fila * CUADRADO_ALTO + CUADRADO_ALTO)
            gamelib.draw_text(juego[fila][columna], CUADRADO_ANCHO * columna + CUADRADO_ANCHO/2, CUADRADO_ALTO * fila + CUADRADO_ALTO/2, fill='black', anchor='c')

def main():
    juego, quien_juega = juego_crear()

    # Ajustar el tamaño de la ventana
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)

    # Mientras la ventana esté abierta:
    while gamelib.is_alive():
        # Todas las instrucciones que dibujen algo en la pantalla deben ir
        # entre `draw_begin()` y `draw_end()`:
        gamelib.draw_begin()
        juego_mostrar(juego, quien_juega)
        gamelib.draw_end()

        # Terminamos de dibujar la ventana, ahora procesamos los eventos (si el
        # usuario presionó una tecla o un botón del mouse, etc).
 
        # Esperamos hasta que ocurra un evento
        ev = gamelib.wait()

        if not ev:
            # El usuario cerró la ventana.
            break

        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            break

        if ev.type == gamelib.EventType.ButtonPress:
            # El usuario presionó un botón del mouse
            x, y = ev.x, ev.y # averiguamos la posición donde se hizo click
            juego,quien_juega = juego_actualizar(juego, x, y,quien_juega)

gamelib.init(main)
