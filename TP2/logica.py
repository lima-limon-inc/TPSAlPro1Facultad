# Imports
from procesar_archivos import leer_movimientos, guardar_tablero, leer_archivo
from random import choice, randint

# Constantes relacionadas con el tablero:
FILAS = 8
COLUMNAS = 8
ULTIMA_FILA = FILAS - 1
ULTIMA_COLUMNA = COLUMNAS - 1
ARCHIVO_GUARDADO = "ultimo_tablero.csv"
ARCHIVO_FAILSAFE = "failsafe.csv"

# Constantes relacionadas con los movimientos
MOVIMIENTOS = leer_movimientos("movimientos.csv")

# Constantes relacionadas con las piezas
PIEZA_ANCHO = 44
PIEZA_LARGO = 44
DIRECTORIO_SPRITES = "sprites/"

# Constantes relacionadas con la ventana
ANCHO_VENTANA = PIEZA_ANCHO * COLUMNAS
ALTO_VENTANA = PIEZA_LARGO * FILAS
COLOR_BLANCO = "#2d2d3f"
COLOR_NEGRO  = "#181818"

# Constantes relacionada con los mensajes en pantalla
TAMANO_TEXTO = 9
ESPACIO_MENSAJE = 50
PRIMERA_COLUMNA = 0 + PIEZA_ANCHO // 2
SEGUNDA_COLUMNA = 4 * PIEZA_ANCHO + PIEZA_ANCHO // 2
PRIMER_FILA_MENSAJES = ALTO_VENTANA +  ESPACIO_MENSAJE // 4
SEGUNDA_FILA_MENSAJES = ALTO_VENTANA + ESPACIO_MENSAJE // 2  + TAMANO_TEXTO

# Constantes relacionadas con el teclado
TECLA_PARA_GUARDAR_TABLERO = "g"
TECLA_PARA_CARGAR_TABLERO = "c"
TECLA_PARA_REINTENTAR = "Z"
TECLA_PARA_CERRAR_JUEGO = "Esc"


class Tablero:
    '''
    La clase Tablero representa el tablero en donde estan las piezas puestas y tiene las funciones relacionadas con el movimiento de las piezas
    '''
    def __init__(self, nivel):
        '''
        Constructor de la clase Tablero, este recibe como parametro el nivel en el que el jugador esta. El nivel determina la cantidad de piezas que va a haber puestas
        Recibe:
            0. nivel -> int. Nivel en el que estas
        Devuelve:
            0. Una instancia de la clase Tablero.
        '''
        self.tablero = {} # El tablero en si mismo es un diccionario con la siguiente escrutcura: (Columna (x), Fila (y)): Pieza


        # El siguiente codigo se encarga de generar el tablero
        #  ----------------------------------------------

        # La posicion de la primera ficha es elegida aleatoriamente
        columna, fila = randint(0,7), randint(0,7)

        self.tablero[columna, fila] = Pieza(columna, fila, choice(list(MOVIMIENTOS.keys()))) #MOVIMIENTOS.keys() son todos los tipos de piezas que el programa leyo en el archivo movimientos.csv.

        self.pieza_seleccionada = (columna, fila) #Hace referencia a la ficha con la que el jugador empieza. EL jugador empieza con la pieza que fue puesta primera

        for i in range(1, nivel + 2): #El "1," se debe a que la primera pieza la genero fuera del for loop
            columna, fila = choice(list(self.tablero[columna, fila].movimientos_validos - self.casillas_ocupadas())) #Elige una posicion aleatoria (dentro de la interseccion entre la posiciones validas de la pieza y las posiciones ocupadas por el tablero) para poner la nueva pieza

            self.tablero[columna, fila] = Pieza(columna, fila, choice(list(MOVIMIENTOS.keys()))) #MOVIMIENTOS.keys() son todos los tipos de piezas que el programa leyo en el archivo movimientos.csv.

        self.failsafe = (self.tablero.copy(), tuple(self.pieza_seleccionada)) #self.failsafe es una tupla que contiene los contenidos del tablero generado y la pieza seleccionada. Esta variable se usa para cuando el usuario tiene que reiniciar el nivel por si no puede seguir

    def actualizar_tablero(self, columna_destino, fila_destino):
        '''
        Funcion que se encarga de actualizar el tablero, cosa que sucede cuando la pieza_seleccionada come otra pieza. En ese momento, la pieza_seleccionada pasa a ser la pieza que fue comida
        Recibe:
            0. columna_destino -> int. Columna donde el usuario hizo click
            1. fila_destino ->. Fila donde el usuario hizo click
        Devuelve:
            0. None
            Es una funcion impura, solo muta el tablero y pieza_seleccionada

        '''
        if (columna_destino, fila_destino) not in self.tablero[self.pieza_seleccionada].movimientos_validos: # Si la casilla seleccionada no esta dentro de los movimientos validos de la pieza, "ignoramos" la accion
            return None
        if (columna_destino, fila_destino) not in self.casillas_ocupadas():#Si la casilla seleccionada esta vacia (es decir que no esta en el diccionario self.tablero) "ignoramos" la accion
            return None

        self.tablero.pop(self.pieza_seleccionada) #Sacamos del tablero la pieza donde estabamos

        self.pieza_seleccionada = (columna_destino, fila_destino) #Asignamos la pieza seleccionada a donde el usuario se "movio" (donde comio la ficha)

    def casillas_ocupadas(self):
        '''
        Funcion que simplemente devuelve todas las posiciones que estan ocupadas por piezas
        Recibe:
            0. None
        Devuelve:
            0. list. Lista con todas las claves del diccionario. Esto representa todas las posiciones ocupadas (Por ejemplo: [(0,3) , (4,6), (3,7)]
        '''
        return self.tablero.keys()

    def resetear_tablero(self):
        '''
        Funcion que hace vacia el tablero
        Recibe:
            0. None
        Devuelve:
            0. None
            Es una funcion impura, solo muta el diccionario self.tablero
        '''
        self.tablero = {}

    def guardar_tablero_actual(self):
        '''
        Funcion que se encarga de guardar el tablero actual, con todos los avances del usuario en un archivo; y el failsafe en otro archivo
        Recibe:
            0. None
        Devuelve:
            0. None
            Funcion impura, solo crea dos archivos
        '''
        guardar_tablero(ARCHIVO_FAILSAFE, self.failsafe[0], self.failsafe[1]) #Guarda el failsafe, por si el usuario tiene que reiniciar en la direccion ARCHIVO_FAILSAFE
        guardar_tablero(ARCHIVO_GUARDADO, self.tablero, self.pieza_seleccionada) #Guarda el tablero y la pieza_seleccionada como lo dejo el usuario

    def cargar_archivo(self):
        '''
        Funcion que se encarga de leer los archivos de guardado por si el usuario y restaurar el estado guardado.
        He de reconocer que no estoy muy satisfecho con esta funcion. Tiene efectos secundarios, abre archivos y devuelve un valor; medio caotica.
        Estoy seguro que debe haber una mejor implementacion; tal vez si almacenase los datos de manera diferente
        Recibe:
            0. None
        Devuelve:
            1. nivel -> int. La funcion devuelve el nivel en donde el usuario guardo el nivel. No es un valor que este guardado en el archivo de guardado, sino que se calcula en el momento restandole 2 a la cantidad de piezas puestas en el tablero guardado en failsafe (que es el tablero en el momento en el que el tablero es generado)
        '''
        self.resetear_tablero()

        tablero, self.pieza_seleccionada = leer_archivo(ARCHIVO_GUARDADO)
        nuevo_tablero = {} #crea un nuevo tablero momentaneo
        for localizacion, constructor in tablero.items():
            fila, columna, tipo = constructor
            nuevo_tablero[localizacion] = Pieza(fila, columna, tipo) #Crea las piezas en el nuevo_tablero

        self.tablero = nuevo_tablero #Iguala el tablero al nuevo_tablero (que tiene todas las piezas ya cargadas). Lo hago en dos partes para evitar que se vea como se van generando las piezas (aunque esto solo pasaria si el tablero tiene muchas piezas, posiblemente mas de la que puede llegar a tener)

        tablero, pieza_seleccionada = leer_archivo(ARCHIVO_FAILSAFE)
        tablero_failsafe = {} #Hace lo mismo que el las lineas anteriores pero para el archivo failsafe
        for localizacion, constructor in tablero.items():
            fila, columna, tipo = constructor
            tablero_failsafe[localizacion] = Pieza(fila, columna, tipo)
        self.failsafe = (tablero_failsafe, pieza_seleccionada)

        return len(self.failsafe[0].keys()) - 2 #Devuelve el nivel

    def reintentar(self):
        '''
        Funcion que se encarga de recargar el nivel por si el usuario se quedo trabado
        Recibe:
            0. None
        Devuelve:
            0. None
            Funcion impura, solo muta el tablero y la pieza_seleccionada
        '''
        self.tablero = self.failsafe[0].copy() #Lo iguala a LOS CONTENIDOS del failsafe, porque sino estarian apuntando a los mismos lugares de la memoria, lo cual modificaria el failsafe. Cosa que no quiero
        self.pieza_seleccionada = tuple(self.failsafe[1])


class Pieza:
    '''
    La clase Pieza representa una pieza (quien lo hubiese dicho).
    Cada pieza puede ser de 1/3 tipos: "caballo, alfil o torre". Si hubiesen mas piezas en el archivo movimientos.csv, tambien podria ser una de estas.
    '''
    def __init__(self,columna, fila, tipo):
        '''
        Constructor de la clase Pieza, esta recibe como parametro la columna y la fila donde va a ser puesta. Sin embargo, la pieza no "guarda" su fila y su columna; ya que ese dato ya esta guardado en la llave del diccionario. La clase en si misma solo guarda su tipo (si es caballo, alfil o torre [o etc[) y un conjunto (set) de todos las posiciones a donde se puede mover
        Recibe:
            0. columa -> int. Representa la columna del tablero
            1. fila -> int. Representa la fila del tablero
            2. tipo -> str. Representa que ficha queremos que sea ("caballo", "alfil", "torre")
        Devuelve:
            0. Una instancia de la clase Pieza.
        '''
        self.tipo = tipo #Hace referencia a que tipo de pieza es (alfil, caballo, etc)

        self.movimientos_validos = self.calcular_movimientos_validos(fila, columna) #

    def __str__(self):
        return f"{self.tipo}"

    def devolver_imagen(self, seleccionado): #Seleccionado quiere decir que es la pieza seleccionada actualmente
        if seleccionado:
            color =  "_rojo.gif"
        else:
            color =  "_blanco.gif"

        return DIRECTORIO_SPRITES + str(self) + color

    def calcular_movimientos_validos(self, fila, columna): #Esta funcion usa como referencia la constante global MOVIMIENTOS. La guarde como constante global ya que es la misma para todas las fichas
        movimientos_validos = set()
        for movimiento in MOVIMIENTOS[str(self)]:
            posibleColumna = columna + movimiento[0]
            posibleFila = fila + movimiento[1]

            if (posibleColumna > ULTIMA_COLUMNA or posibleColumna < 0) or (posibleFila > ULTIMA_FILA or posibleFila < 0): #Si se cumple esta condicion, significa que dicha posicion esta fuera de rango del tablero
                continue

            posibleMovimiento = (posibleColumna, posibleFila)

            movimientos_validos.add(posibleMovimiento)

        return movimientos_validos
