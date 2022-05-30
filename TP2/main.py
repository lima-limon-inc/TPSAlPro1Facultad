import gamelib
from logica import *


class Game:
    def __init__(self, nivel):
        self.nivel = nivel
        self.tablero = Tablero(self.nivel)

    def siguiente_nivel(self):
        self.nivel += 1
        self.tablero = Tablero(self.nivel)

    def de_click_a_diccionario(self, coord_x, coord_y):
        columna = coord_x // PIEZA_ANCHO
        fila = coord_y // PIEZA_LARGO

        return columna, fila

    def mostrar(self):
        for fila in range(FILAS):
            pintar_blanco = (False if fila % 2 ==0 else True)

            for columna in range(COLUMNAS):
                pintar_blanco = not pintar_blanco
                color_celda = (COLOR_BLANCO if pintar_blanco else COLOR_NEGRO)

                gamelib.draw_rectangle(PIEZA_ANCHO * columna, PIEZA_LARGO * fila, PIEZA_ANCHO * columna + PIEZA_ANCHO, fila * PIEZA_LARGO + PIEZA_LARGO, fill=color_celda, width=4) # Funcion que se encarga de pintar los cuadraditos del tablero de ajedrez

                if (columna, fila) not in self.tablero.tablero:
                    continue #Una vez dibujados la cuadricula, solo nos interesa dibujar las piezas. Si no hay una pieza en la coordenada actual, vamos al siguiente ciclo

                gamelib.draw_image(self.tablero.tablero[(columna,fila)].devolver_imagen((True if (columna, fila) == self.tablero.pieza_seleccionada else False)), columna * 44, fila * 44)

                if (columna, fila) in self.tablero.tablero[self.tablero.pieza_seleccionada].movimientos_validos: # Si la pieza que va a dibujar se encuentra en algunas de los lugares donde la pieza seleccionada se puede mover, dibujamos un rectangulo rojo
                    gamelib.draw_rectangle(columna * 44 + 3, fila * 44 + 3, columna * 44 + 41, fila * 44 +41,fill = "" , outline="#db0404", width=2)

        gamelib.draw_end()

def main():
    gamelib.title("Shape Shifter Chess")
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)

    juego = Game(1)

    while gamelib.is_alive():
        juego.mostrar()

        ev = gamelib.wait()
        if not ev:
            break

        if ev.type == gamelib.EventType.ButtonPress and ev.mouse_button == 1:
            print(f'se ha presionado el botón del mouse: {ev.x} {ev.y}')
            columna, fila = juego.de_click_a_diccionario(ev.x, ev.y)
            print(columna, fila)
            juego.tablero.actualizar_tablero(columna, fila)


        elif ev.type == gamelib.EventType.KeyPress:
            print(f'se ha presionado la tecla: {ev.key}')

gamelib.init(main)
