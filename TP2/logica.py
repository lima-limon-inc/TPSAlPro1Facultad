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

class Tablero:
    def __init__(self):
        self.tablero = {} # (Columna (x), Fila (y)): Pieza
        self.tablero_mutable = {}
        self.nivel = 2

    def actualizar_tablero(self, columna, fila, pieza):
        if columna > ULTIMA_COLUMNA or columna < 0:
            raise IndexError(f"Error, {columna} no es una columna valida, el tablero es de {FILAS} x {COLUMNAS}; y la ultima columna valida es {ULTIMA_COLUMNA}")
        elif fila > ULTIMA_FILA or fila < 0:
            raise IndexError(f"Error, {fila} no es una columna valida, el tablero es de {FILAS} x {COLUMNAS}; y la ultima fila valida es {ULTIMA_FILA}") #Estos dos errores no deberian ocurrir, pero si llegan a ocurrir, se tiene que crashear el programa para evitar un comportamiento no deseado

        self.tablero_mutable[(columna, fila)] = pieza
        
        #return self.tablero_mutable

    def casillas_ocupadas(self):
        return self.tablero_mutable.keys()

    def generar_tablero(self):
        columna = randint(0,7)
        fila = randint(0,7)
        print(f"DEBUG Aleatorio: {columna} {fila}")
        for i in range(self.nivel + 2):
            self.tablero[columna, fila] = Pieza(choice(list(MOVIMIENTOS.keys())), False) #MOVIMIENTOS.keys() son todos los tipos de piezas
            columna, fila = choice(list(self.tablero[columna, fila].calcular_movimientos_validos(columna, fila)))
       #    print(columna)
       #    print(fila)
       #
       #print(self.tablero)

            



class Pieza:
    def __init__(self, tipo, seleccionado):
        self.tipo = tipo
        self.seleccionado = seleccionado #Booleano
        self.imagen = self.cambiar_imagen(seleccionado)
        self.movimientos_validos = set()  #TODO: Posiblemente borrar

    def __str__(self):
        return f"{self.tipo}"

    def cambiar_imagen(self, seleccionado):
        if seleccionado:
            return str(self) + "_rojo.gif"
        else:
            return str(self) + "_blanco.gif"

    def calcular_movimientos_validos(self, columna, fila): #, casillas, movimientoJugador): #Esta funcion usa como referencia la constante global MOVIMIENTOS. La guarde como constante global ya que es la misma para todas las fichas
        movimientos_validos = set()
        for movimiento in MOVIMIENTOS[str(self)]:
            posibleColumna = columna + movimiento[0]
            posibleFila = fila + movimiento[1]

            if (posibleColumna > 7 or posibleColumna < 0) or (posibleFila > 7 or posibleFila < 0):
                continue

            posibleMovimiento = (posibleColumna, posibleFila)

            movimientos_validos.add(posibleMovimiento)
            
        
        print(f"DEBUG MOVIMIENTOS VALIDOS {self}: {movimientos_validos}")
        return movimientos_validos

#c = Pieza("alfil", False)
#c.calcular_movimientos_validos((6,6))
#print(c.movimientos_validos)




t = Tablero()
t.generar_tablero()

for posicion, pieza in t.tablero.items():
    print(posicion, pieza)
