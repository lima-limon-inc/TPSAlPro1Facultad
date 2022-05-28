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



class Tablero:
    def __init__(self):
        self.tablero = {} # (Columna (x), Fila (y)): Pieza
        self.tablero_mutable = {}
        self.nivel = 1 #Primer nivel

        # El siguiente codigo se encarga de generar el tablero
        #  ----------------------------------------------

        # La primera ficha es elegida aleatoriamente
        columna = randint(0,7)
        fila = randint(0,7)
        self.tablero[columna, fila] = Pieza(choice(list(MOVIMIENTOS.keys())), True) #MOVIMIENTOS.keys() son todos los tipos de piezas que el programa leyo en el archivo movimientos.csv

        self.pieza_seleccionada = (columna, fila) #Hace referencia a la ficha con la que el jugador empieza

        for i in range(1, self.nivel + 2): #El "1," se debe a que la primera pieza la genero fuera del for loop
            columna, fila = choice(list(self.tablero[columna, fila].calcular_movimientos_validos(columna, fila, self.casillas_ocupadas())))

            self.tablero[columna, fila] = Pieza(choice(list(MOVIMIENTOS.keys())), False) #MOVIMIENTOS.keys() son todos los tipos de piezas

        self.tablero_mutable = dict(self.tablero) #El tablero mutable es donde el usuario interactua, el tablero no muta (se usa como "failsafe" por si el jugador se queda trabado

    def actualizar_tablero(self, columna_movida, fila_movida):
        """Funcion que toma una ficha de la posicion (x1,y1) y la lleva a la posicion (x2,y2)""" 
        if columna_movida > ULTIMA_COLUMNA or columna_movida < 0:
            raise IndexError(f"Error, {columna} no es una columna valida, el tablero es de {FILAS} x {COLUMNAS}; y la ultima columna valida es {ULTIMA_COLUMNA}")
        elif fila_movida > ULTIMA_FILA or fila_movida < 0:
            raise IndexError(f"Error, {fila} no es una columna valida, el tablero es de {FILAS} x {COLUMNAS}; y la ultima fila valida es {ULTIMA_FILA}") #Estos dos errores no deberian ocurrir, pero si llegan a ocurrir, se tiene que crashear el programa para evitar un comportamiento no deseado
        self.tablero_mutable.pop(self.pieza_seleccionada)
        
        self.pieza_seleccionada = (columna_movida, fila_movida)

    def casillas_ocupadas(self):
        return self.tablero.keys()

    def generar_tablero(self):
        columna = randint(0,7)
        fila = randint(0,7)
        self.tablero[columna, fila] = Pieza(choice(list(MOVIMIENTOS.keys())), True) #MOVIMIENTOS.keys() son todos los tipos de piezas que el programa leyo en el archivo movimientos.csv
        self.pieza_seleccionada = (columna, fila)

        #print(f"DEBUG Aleatorio: {columna} {fila}")
        for i in range(1, self.nivel + 2): #El "1," se debe a que la primera pieza la genero fuera del for loop
            columna, fila = choice(list(self.tablero[columna, fila].calcular_movimientos_validos(columna, fila, self.casillas_ocupadas())))

            self.tablero[columna, fila] = Pieza(choice(list(MOVIMIENTOS.keys())), False) #MOVIMIENTOS.keys() son todos los tipos de piezas

        self.tablero_mutable = dict(self.tablero) #El tablero mutable es donde el usuario interactua, el tablero no muta (se usa como "failsafe" por si el jugador se queda trabado

class Pieza:
    def __init__(self, tipo, seleccionado):
        self.tipo = tipo
        self.seleccionado = seleccionado #Booleano
        self.imagen = self.devolver_imagen(self.seleccionado)
        self.movimientos_validos = set()  #TODO: Posiblemente borrar
        print(f"DEBUG {self.tipo} CREADO. Movimientos {self.movimientos_validos}")

    def __str__(self):
        return f"{self.tipo}"

    def devolver_imagen(self, seleccionado):
        if seleccionado:
            color =  "_rojo.gif"
        else:
            color =  "_blanco.gif"

        return DIRECTORIO_SPRITES + str(self) + color

    def calcular_movimientos_validos(self, columna, fila, casillas_ocupadas): #, casillas, movimientoJugador): #Esta funcion usa como referencia la constante global MOVIMIENTOS. La guarde como constante global ya que es la misma para todas las fichas
        movimientos_validos = set()
        for movimiento in MOVIMIENTOS[str(self)]:
            posibleColumna = columna + movimiento[0]
            posibleFila = fila + movimiento[1]

            if (posibleColumna > 7 or posibleColumna < 0) or (posibleFila > 7 or posibleFila < 0):
                continue

            posibleMovimiento = (posibleColumna, posibleFila)

            if posibleMovimiento in casillas_ocupadas: #Chequea que no haya dos piezas en el mismo lugar
                continue


            movimientos_validos.add(posibleMovimiento)
            
        
        self.movimientos_validos = movimientos_validos #TODO: Posiblemente arreglar
        return movimientos_validos
