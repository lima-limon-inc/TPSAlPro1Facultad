# Imports
from procesar_archivos import leer_movimientos
from random import choice, randint

# Constantes relacionadas con el tablero:
FILAS = 8
COLUMNAS = 8
ULTIMA_FILA = FILAS - 1
ULTIMA_COLUMNA = COLUMNAS - 1

# Constantes relacionadas con los movimientos
MOVIMIENTOS = leer_movimientos("movimientos.csv")

# Constantes relacionadas con las piezas
PIEZA_ANCHO = 44
PIEZA_LARGO = 44
DIRECTORIO_SPRITES = "sprites/"

# Constantes relacionadas con la ventana
ESPACIO_MENSAJE = 50
ANCHO_VENTANA = PIEZA_ANCHO * COLUMNAS
ALTO_VENTANA = PIEZA_LARGO * FILAS
COLOR_BLANCO = "#2d2d3f"
COLOR_NEGRO  = "#181818"



class Game:
    def __init__(self, nivel):
        self.nivel = nivel
        self.tablero = Tablero(self.nivel)

    def siguienteNivel(self):
        self.nivel += 1
        self.tablero = Tablero(self.nivel)

    def procesar_clicks(self, coord_x, coord_y):
        for columna in range(COLUMNAS): #Funcion que transforma las coordenadas x e y del mouse en coordenadas de la lista. Ejemplo:  (x: 113, y:237) --> (x: 3, y:7)
            if not (columna * CUADRADO_ANCHO <= x <= columna * CUADRADO_ANCHO + CUADRADO_ANCHO): 
                continue
            x = columna
            for fila in range(FILAS):
                if not (fila * CUADRADO_ALTO <= y <= fila * CUADRADO_ALTO + CUADRADO_ALTO):
                    continue
                y = fila



class Tablero:
    def __init__(self, nivel):
        self.tablero = {} # (Columna (x), Fila (y)): Pieza
        # El siguiente codigo se encarga de generar el tablero
        #  ----------------------------------------------

        # La primera ficha es elegida aleatoriamente
        columna, fila = randint(0,7), randint(0,7)

        self.tablero[columna, fila] = Pieza(columna, fila, choice(list(MOVIMIENTOS.keys())), True, self.casillas_ocupadas()) #MOVIMIENTOS.keys() son todos los tipos de piezas que el programa leyo en el archivo movimientos.csv. Empieza en True, porque la primera pieza generada es con la que el jugador empieza

        self.pieza_seleccionada = (columna, fila) #Hace referencia a la ficha con la que el jugador empieza

        for i in range(1, nivel + 2): #El "1," se debe a que la primera pieza la genero fuera del for loop
            columna, fila = choice(list(self.tablero[columna, fila].movimientos_validos)) #Elige una posicion dentro de las posiciones validas de la ultima pieza, para poner la nueva pieza

            self.tablero[columna, fila] = Pieza(columna, fila, choice(list(MOVIMIENTOS.keys())), False, self.casillas_ocupadas()) #MOVIMIENTOS.keys() son todos los tipos de piezas que el programa leyo en el archivo movimientos.csv. Empieza en True, porque la primera pieza generada es con la que el jugador empieza


        self.failsafe = (dir(self.tablero), tuple(self.pieza_seleccionada))

    def actualizar_tablero(self, columna_destino, fila_destino):
        """Funcion que toma una ficha de la posicion (x1,y1) y la lleva a la posicion (x2,y2)"""
        if columna_destino > ULTIMA_COLUMNA or columna_destino < 0:
            raise IndexError(f"Error, {columna} no es una columna valida, el tablero es de {FILAS} x {COLUMNAS}; y la ultima columna valida es {ULTIMA_COLUMNA}")
        elif fila_destino > ULTIMA_FILA or fila_destino < 0:
            raise IndexError(f"Error, {fila} no es una columna valida, el tablero es de {FILAS} x {COLUMNAS}; y la ultima fila valida es {ULTIMA_FILA}") #Estos dos errores no deberian ocurrir, pero si llegan a ocurrir, se tiene que crashear el programa para evitar un comportamiento no deseado

        if not self.tablero_mutable[columna_destino, fila_destino].seleccionado:
            self.tablero_mutable[columna_destino, fila_destino].hacer_activa()

        self.tablero_mutable.pop(self.pieza_seleccionada)

        self.pieza_seleccionada = (columna_destino, fila_destino)

    def casillas_ocupadas(self):
        return self.tablero.keys()

class Pieza:
    def __init__(self,columna, fila, tipo, seleccionado, casillas_ocupadas):
        self.fila = fila
        self.columna = columna

        self.tipo = tipo #Hace referencia a que tipo de pieza es (alfil, caballo, etc)

        self.seleccionado = seleccionado #Booleano, representa si la pieza esta seleccionada. En todo momento deberia haber solo 1 pieza seleccionada

        self.imagen = self.devolver_imagen(self.seleccionado) # La funcion devuelve la imagen, dependiendo de si la ficha fue seleccionada o no

        self.movimientos_validos = self.calcular_movimientos_validos(fila, columna, casillas_ocupadas) #

    def __str__(self):
        return f"{self.tipo}"

    def hacer_activa(self):
        self.seleccionado = True

    def devolver_imagen(self, seleccionado):
        if seleccionado:
            color =  "_rojo.gif"
        else:
            color =  "_blanco.gif"

        return DIRECTORIO_SPRITES + str(self) + color

    def calcular_movimientos_validos(self, fila, columna, casillas_ocupadas): #Esta funcion usa como referencia la constante global MOVIMIENTOS. La guarde como constante global ya que es la misma para todas las fichas
        movimientos_validos = set()
        for movimiento in MOVIMIENTOS[str(self)]:
            posibleColumna = columna + movimiento[0]
            posibleFila = fila + movimiento[1]

            if (posibleColumna > ULTIMA_COLUMNA or posibleColumna < 0) or (posibleFila > ULTIMA_FILA or posibleFila < 0): #Si se cumple esta condicion, significa que dicha posicion esta fuera de rango del tablero
                continue

            posibleMovimiento = (posibleColumna, posibleFila)

            if posibleMovimiento in casillas_ocupadas: #Chequea que no haya dos piezas en el mismo lugar
                continue

            movimientos_validos.add(posibleMovimiento)

        return movimientos_validos

