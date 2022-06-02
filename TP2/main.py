import gamelib
from logica import *


class Game:
    def __init__(self, nivel, titulo, ancho, largo):
        self.nivel = nivel
        self.titulo = titulo
        self.ancho = ancho
        self.largo = largo
        self.tecla_restar = TECLA_PARA_CARGAR_TABLERO
        self.tecla_guardar = TECLA_PARA_GUARDAR_TABLERO
        self.tecla_salir = TECLA_PARA_CERRAR_JUEGO
        self.tecla_reintentar = TECLA_PARA_REINTENTAR
        self.tablero = Tablero(self.nivel)

    def siguiente_nivel(self):
        self.nivel += 1
        self.tablero = Tablero(self.nivel)

    def de_click_a_diccionario(self, coord_x, coord_y):
        columna = coord_x // PIEZA_ANCHO
        fila = coord_y // PIEZA_LARGO

        return columna, fila

    def mostrar(self):
        gamelib.draw_text(self.titulo, 0 + PIEZA_ANCHO //2 , PRIMER_FILA_MENSAJES, anchor="w", bold=True, size = TAMANO_TEXTO) #Dibuja el titulo del juego
        gamelib.draw_text(f"Nivel: {self.nivel}", 0 + PIEZA_ANCHO //2 , SEGUNDA_FILA_MENSAJES, anchor="w", bold=True, size = TAMANO_TEXTO) #Dibuja el nivel actual
        gamelib.draw_text(f"Salir: {self.tecla_salir}", SEGUNDA_COLUMNA, PRIMER_FILA_MENSAJES, anchor="w", bold=True, size=TAMANO_TEXTO)
        gamelib.draw_text(f"Reintentar: {self.tecla_reintentar}", SEGUNDA_COLUMNA, SEGUNDA_FILA_MENSAJES, anchor="w", bold=True, size=TAMANO_TEXTO)

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

    def main(self):
        gamelib.title(juego.titulo) #Le pone el titulo a la ventana, el cual coincide con el titulo de la clase Game
        gamelib.resize(juego.ancho, juego.largo)

        while gamelib.is_alive():

            gamelib.draw_begin()
            juego.mostrar()
            gamelib.draw_end()

            ev = gamelib.wait()
            if not ev:
                break

            if ev.type == gamelib.EventType.ButtonPress and ev.mouse_button == 1: #El usuario apreto el click izquierdo
                columna, fila = juego.de_click_a_diccionario(ev.x, ev.y)

                juego.tablero.actualizar_tablero(columna, fila)
                if len(juego.tablero.tablero.keys()) <= 1: #Si solo hay 1 pieza, pasar al siguiente nivel (El menor esta puesto por si hay algun error de procesamiento(?) auqnue no deberia suceder)
                    juego.siguiente_nivel()

            elif ev.type == gamelib.EventType.KeyPress:
                if ev.key == "p":
                    print("apretaste p")
                    juego.tablero.guardar_tablero_actual()

                elif ev.key == "c":
                   #print("apretaste c")
                    juego.tablero.cargar_archivo()


juego = Game(1, "SHAPE SHIFTER CHESS",ANCHO_VENTANA, ALTO_VENTANA + ESPACIO_MENSAJE )
gamelib.init(juego.main)
