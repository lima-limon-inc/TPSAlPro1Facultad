
# Constantes relacionadas con el tablero:
FILAS = 8
COLUMNAS = 8
ULTIMA_FILA = FILAS - 1
ULTIMA_COLUMNA = COLUMNAS - 1

class Tablero:
    def __init__(self):
        self.tablero = {} # (Columna (x), Fila (y)): Pieza
        self.tablero_mutable = {}

    def actualizar_tablero(self, columna, fila, pieza):
        if columna > ULTIMA_COLUMNA or columna < 0:
            raise IndexError(f"Error, {columna} no es una columna valida, el tablero es de {FILAS} x {COLUMNAS}; y la ultima columna valida es {ULTIMA_COLUMNA}")
        elif fila > ULTIMA_FILA or fila < 0:
            raise IndexError(f"Error, {fila} no es una columna valida, el tablero es de {FILAS} x {COLUMNAS}; y la ultima fila valida es {ULTIMA_FILA}") #Estos dos errores no deberian ocurrir, pero si llegan a ocurrir, se tiene que crashear el programa para evitar un comportamiento no deseado

        self.tablero_mutable[(columna, fila)] = pieza
        
        return self.tablero_mutable

    
