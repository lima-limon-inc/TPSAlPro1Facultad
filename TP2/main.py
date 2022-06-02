from logica import *

class Game:
    ''':w
    La clase Game representa el "juego" en si mismo, todo lo que involucra la interaccion con el usuario. No representa ningun objeto en particular. Sino mas un "meta" objeto
    '''
    def __init__(self, nivel, titulo, ancho, largo):
        '''
        Constructor de la clase Game, recibe
        Recibe:
            0. nivel -> int. Nivel en el que estas
        Devuelve:
            0. Una instancia de la clase Tablero.G
        '''
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
        '''
        Funcion que se invoca cuando el usuario completa el nivel actual.
        Recibe:
            0. None
        Devuelve:
            0. None
            Funcion impura, muta el estado del nivel y genera un nuevo tablero
        '''
        self.nivel += 1
        self.tablero = Tablero(self.nivel)

    def de_click_a_diccionario(self, coord_x, coord_y):
        '''
        Funcion que transforma los clicks del usuario a la casilla del tablero correspondiente
        Recibe:
            0. coord_x -> int. Coordenada x del click
            1. coord_y -> int. Coordenada y del click
        Devuelve:
            0. columa -> int. Columna correspondiente del tablero
            1. fila -> int. Fila correspondiente del tablero
        '''
        columna = coord_x // PIEZA_ANCHO
        fila = coord_y // PIEZA_LARGO

        if fila > ULTIMA_COLUMNA or columna > ULTIMA_FILA: #Si el usuario hace click fuera del tablero, devolvemos (None, None) para que este click sea ignorado
            columna, fila = None, None

        return columna, fila

    def mostrar(self):
        '''
        Funcion que se encarga de mostrar la representacion grafica del programa
        Recibe:
            0. None
        Devuele:
            0. None
            Funcion impura, solo tiene efectos secundarios
        '''
        gamelib.draw_begin()
        gamelib.draw_text(self.titulo, 0 + PIEZA_ANCHO //2 , PRIMER_FILA_MENSAJES, anchor="w", bold=True, size = TAMANO_TEXTO) #Dibuja el titulo del juego
        gamelib.draw_text(f"Nivel: {self.nivel}", 0 + PIEZA_ANCHO //2 , SEGUNDA_FILA_MENSAJES, anchor="w", bold=True, size = TAMANO_TEXTO) #Dibuja el nivel actual
        gamelib.draw_text(f"Salir: {self.tecla_salir}", SEGUNDA_COLUMNA, PRIMER_FILA_MENSAJES, anchor="w", bold=True, size=TAMANO_TEXTO)
        gamelib.draw_text(f"Reintentar: {self.tecla_reintentar}", SEGUNDA_COLUMNA, SEGUNDA_FILA_MENSAJES, anchor="w", bold=True, size=TAMANO_TEXTO)

        for fila in range(FILAS):
            pintar_blanco = (False if fila % 2 ==0 else True) #El valor de "pintar_blanco" esta "al reves". Esto se debe a que lo primero que hace el siguiente for loop es "switchear" el valor de pintar_blanco; por eso pintar_blanco empieza como "False" a pesar de que la primera casilla SI se tiene que pintar de blanco. Esto se podria poner "al derecho" (True if fila % 2 ==0 else False) si pusiese el switch de pintar_blanco al FINAL del siguiente for loop; pero preferi dejarlo "al reves" asi todas las menciones de pintar_blanco estan una al lado de la otra.

            for columna in range(COLUMNAS):
                pintar_blanco = not pintar_blanco
                color_celda = (COLOR_BLANCO if pintar_blanco else COLOR_NEGRO)

                gamelib.draw_rectangle(PIEZA_ANCHO * columna, PIEZA_LARGO * fila, PIEZA_ANCHO * columna + PIEZA_ANCHO, fila * PIEZA_LARGO + PIEZA_LARGO, fill=color_celda, width=4) # Funcion que se encarga de pintar los cuadraditos del tablero de ajedrez

                if (columna, fila) not in self.tablero.tablero:
                    continue #Una vez dibujados la cuadricula, solo nos interesa dibujar las piezas. Si no hay una pieza en la coordenada actual, vamos al siguiente ciclo

                gamelib.draw_image(self.tablero.tablero[(columna,fila)].devolver_imagen((True if (columna, fila) == self.tablero.pieza_seleccionada else False)), columna * PIEZA_ANCHO, fila * PIEZA_LARGO)

                if (columna, fila) in self.tablero.tablero[self.tablero.pieza_seleccionada].movimientos_validos: # Si la pieza que va a dibujar se encuentra en algunas de los lugares donde la pieza seleccionada se puede mover, dibujamos un rectangulo rojo
                    gamelib.draw_rectangle(columna * PIEZA_ANCHO + 3, fila * PIEZA_LARGO + 3, columna * PIEZA_ANCHO + 41, fila * PIEZA_LARGO +41,fill = "" , outline=COLOR_ROJO, width=2) # Los +3 y +41 son "correctores" para que quede correcto el cuadrado rojo alrededor de las piezas
        gamelib.draw_end()

    def pantalla_inicio(self):
        '''
        Funcion que "recibe" al usuario y le pregunta si quiere cargar la partida guardada. Ademas le informa sobre el funcionamiento de algunas de las teclas del teclado.
        Recibe:
            0. None
        Devuele:
            0. None
            Funcion impropia, solo tiene efectos secundarios
        '''
        gamelib.say(f"Bienvenido a {self.titulo}.\nPodes apretar '{TECLA_PARA_GUARDAR_TABLERO}' en cualquier momento para guardar la partida y seguirla mas tarde")
        respuesta = ""
        mensaje = "Partida guardada encontrada, queres seguir desde ahi? (Si/No)"
        if os.path.exists(ARCHIVO_GUARDADO): #El programa solo te pregunta si queres cargar tu partida si *existe* una partida cargada
            while True:
                respuesta = gamelib.input(mensaje)
                if respuesta == None:
                    respuesta = "no"
                respuesta = respuesta.lower()
                if respuesta == "si" or respuesta == "no":
                    break
                mensaje = "Partida guardada encontrada, queres seguir desde ahi? (Si/No) \nPorfavor ingresa 'Si' o 'No'"
            if respuesta == "si":
                self.nivel = self.tablero.cargar_archivo()


    def main(self):
        '''
        Funcion principal del programa. Esta se encarga de procesar todos los clicks del usaurio, en las respectivas posiciones y de asociarlo con la respectiva funcion
        Recibe:
            0. None
        Devuele:
            0. None
            Funcion impropia, solo tiene efectos secundarios
        '''
        self.pantalla_inicio()

        gamelib.title(juego.titulo) #Le pone el titulo a la ventana, el cual coincide con el titulo de la clase Game
        gamelib.resize(juego.ancho, juego.largo)# le da el tamano a la ventana

        while gamelib.is_alive():

            juego.mostrar()

            ev = gamelib.wait()
            if not ev:
                break

            if ev.type == gamelib.EventType.ButtonPress and ev.mouse_button == 1: #El usuario apreto el click izquierdo
                columna, fila = juego.de_click_a_diccionario(ev.x, ev.y)
                if columna == None and fila == None: #El usuario hizo click fuera del tablero. Si esto paso, ignoramos este click
                    continue

                juego.tablero.actualizar_tablero(columna, fila)
                if len(juego.tablero.tablero.keys()) <= 1: #Si solo hay 1 pieza, pasar al siguiente nivel (El menor esta puesto por si hay algun error de procesamiento(?) auqnue no deberia suceder)
                    juego.siguiente_nivel()

            elif ev.type == gamelib.EventType.KeyPress:
                if ev.key == TECLA_PARA_GUARDAR_TABLERO:
                    juego.tablero.guardar_tablero_actual()

                elif ev.key == TECLA_PARA_REINTENTAR:
                    juego.tablero.reintentar()

                elif ev.key == TECLA_PARA_CERRAR_JUEGO:
                    break

juego = Game(1, "SHAPE SHIFTER CHESS",ANCHO_VENTANA, ALTO_VENTANA + ESPACIO_MENSAJE )
gamelib.init(juego.main)
