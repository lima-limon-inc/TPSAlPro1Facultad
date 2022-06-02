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
    def __init__(self, nivel):
        self.tablero = {} # (Columna (x), Fila (y)): Pieza

        # El siguiente codigo se encarga de generar el tablero
        #  ----------------------------------------------

        # La primera ficha es elegida aleatoriamente
        columna, fila = randint(0,7), randint(0,7)

        self.tablero[columna, fila] = Pieza(columna, fila, choice(list(MOVIMIENTOS.keys()))) #MOVIMIENTOS.keys() son todos los tipos de piezas que el programa leyo en el archivo movimientos.csv. Empieza en True, porque la primera pieza generada es con la que el jugador empieza

        self.pieza_seleccionada = (columna, fila) #Hace referencia a la ficha con la que el jugador empieza

        for i in range(1, nivel + 2): #El "1," se debe a que la primera pieza la genero fuera del for loop
            columna, fila = choice(list(self.tablero[columna, fila].movimientos_validos - self.casillas_ocupadas())) #Elige una posicion dentro de las posiciones validas de la ultima pieza, para poner la nueva pieza

            self.tablero[columna, fila] = Pieza(columna, fila, choice(list(MOVIMIENTOS.keys()))) #MOVIMIENTOS.keys() son todos los tipos de piezas que el programa leyo en el archivo movimientos.csv. Empieza en True, porque la primera pieza generada es con la que el jugador empieza

        self.failsafe = (self.tablero.copy(), tuple(self.pieza_seleccionada))

    def actualizar_tablero(self, columna_destino, fila_destino):
        """Funcion que toma una ficha de la posicion (x1,y1) y la lleva a la posicion (x2,y2)"""
        if columna_destino > ULTIMA_COLUMNA or columna_destino < 0:
            raise IndexError(f"Error, {columna} no es una columna valida, el tablero es de {FILAS} x {COLUMNAS}; y la ultima columna valida es {ULTIMA_COLUMNA}")
        elif fila_destino > ULTIMA_FILA or fila_destino < 0:
            raise IndexError(f"Error, {fila} no es una columna valida, el tablero es de {FILAS} x {COLUMNAS}; y la ultima fila valida es {ULTIMA_FILA}") #Estos dos errores no deberian ocurrir, pero si llegan a ocurrir, se tiene que crashear el programa para evitar un comportamiento no deseado

        if (columna_destino, fila_destino) not in self.tablero[self.pieza_seleccionada].movimientos_validos:
            return None
        if (columna_destino, fila_destino) not in self.casillas_ocupadas():
            return None

       #if not self.tablero[columna_destino, fila_destino].seleccionado:
       #    self.tablero[columna_destino, fila_destino].hacer_activa()

        self.tablero.pop(self.pieza_seleccionada)

        self.pieza_seleccionada = (columna_destino, fila_destino)

    def casillas_ocupadas(self):
        return self.tablero.keys()

    def resetear_tablero(self):
        self.tablero = {}

    def guardar_tablero_actual(self):
        guardar_tablero(ARCHIVO_FAILSAFE, self.failsafe[0], self.failsafe[1]) #Guarda el archivo failsafe, por si el usuario tiene que reiniciar
        guardar_tablero(ARCHIVO_GUARDADO, self.tablero, self.pieza_seleccionada) #Guarda el archivo failsafe, por si el usuario tiene que reiniciar

    def cargar_archivo(self):
        self.resetear_tablero()
        tablero, self.pieza_seleccionada = leer_archivo(ARCHIVO_GUARDADO)
        nuevo_tablero = {}
        for localizacion, constructor in tablero.items():
            fila, columna, tipo = constructor
            nuevo_tablero[localizacion] = Pieza(fila, columna, tipo)

        self.tablero = nuevo_tablero

        tablero, pieza_seleccionada = leer_archivo(ARCHIVO_GUARDADO)
        tablero_failsafe = {}
        for localizacion, constructor in tablero.items():
            fila, columna, tipo = constructor
            tablero_failsafe[localizacion] = Pieza(fila, columna, tipo)
        self.failsafe = (tablero_failsafe, pieza_seleccionada)

    def reintentar(self):
        self.tablero = self.failsafe[0]
        self.pieza_seleccionada = self.failsafe[1]


class Pieza:
    def __init__(self,columna, fila, tipo):
        self.tipo = tipo #Hace referencia a que tipo de pieza es (alfil, caballo, etc)

        self.movimientos_validos = self.calcular_movimientos_validos(fila, columna) #

    def __str__(self):
        return f"{self.tipo}"

    def devolver_imagen(self, seleccionado):
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

