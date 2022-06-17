import random
from pila import Pila

class Flood:
    """
    Clase para administrar un tablero de N colores.
    """

    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho
        """
        Genera un nuevo Flood de un mismo color con las dimensiones dadas.

        Argumentos:
            alto, ancho (int): Tamaño de la grilla.
        """
        # Parte 1: Cambiar el `raise` por tu código...
        self.tablero = {}

        for y in range(self.alto):
            for x in range(self.ancho):
                self.tablero[x,y] = 0

        self.direcciones = {
                (0,1), #Abajo
                (0,-1),#Arriba
                (1,0), #Derecha
                (-1,0),#Izquierda
                }

        self.coordenadas_cambiadas = [ (0,0) ]
        self.historial_movimientos = Pila()

    def mezclar_tablero(self, n_colores):
        """
        Asigna de forma completamente aleatoria hasta `n_colores` a lo largo de
        las casillas del tablero.

        Argumentos:
            n_colores (int): Cantidad maxima de colores a incluir en la grilla.
        """
        # Parte 1: Cambiar el `raise` por tu código...
        self.n_colores = n_colores #Me guardo la cantidad de colores

        for y in range(self.alto):
            for x in range(self.ancho):
                self.tablero[x,y] = random.randint(0, n_colores - 1)



    def obtener_color(self, col, fil):
        """
        Devuelve el color que se encuentra en las coordenadas solicitadas.

        Argumentos:
            fil, col (int): Posiciones de la fila y columna en la grilla.

        Devuelve:
            Color asignado.
        """
        # Parte 1: Cambiar el `raise` por tu código...
        return self.tablero.get((col,fil), -1) # El -1 funciona de centinela. Si el color es igual a -1, significa que estamos fuera de la tabla


    def obtener_posibles_colores(self):
        """
        Devuelve una secuencia ordenada de todos los colores posibles del juego.
        La secuencia tendrá todos los colores posibles que fueron utilizados
        para generar el tablero, sin importar cuántos de estos colores queden
        actualmente en el tablero.

        Devuelve:
            iterable: secuencia ordenada de colores.
        """
        # Parte 1: Cambiar el `raise` por tu código...
        return [i for i in range(self.n_colores)]

    def dimensiones(self):
        """
        Dimensiones de la grilla (filas y columnas)

        Devuelve:
            (int, int): alto y ancho de la grilla en ese orden.
        """
        # Parte 1: Cambiar el `raise` por tu código...
        return self.alto, self.ancho


    def moverse(self, desde, hasta, color_actual, color_nuevo):
        if self.obtener_color(hasta[0], hasta[1]) != color_actual:
            return

        self.tablero[hasta] = color_nuevo
        print(hasta)
        print()
        self.coordenadas_cambiadas.append(hasta)


        de_donde_vengo = {(-1 * abs(desde[0] - hasta[0]), -1 * abs(desde[1] - hasta[1]))}

        a_donde_voy = self.direcciones - de_donde_vengo

        for tupla in a_donde_voy:
            self.moverse(hasta, ((hasta[0] + tupla[0]), (hasta[1] + tupla[1])), color_actual, color_nuevo)


        '''
        Si vengo de la derecha, no tengo que chequear la izquierda. Si vengo de arriba, no tengo que chequear abajo
        '''

    def cambiar_color(self, color_nuevo):

        color_actual = self.obtener_color(0,0)
        if color_actual == color_nuevo: #Si el color nuevo es igual al actual, entonces no hay nada que cambiar. En esos casos devolvemos None --> "Los salteamos"
            return "Ignorar"

        self.tablero[0, 0] = color_nuevo

        self.moverse((0,0),(1,0), color_actual, color_nuevo) # La funcion moverse toma como parametro la celda de partida, por eso es llamada dos veces (ya que (0,0) tiene dos celdas adyacentes, las cuales son
        self.moverse((0,0),(0,1), color_actual, color_nuevo) # las que le van a dar comienzo a la recursion. Se podria llamar una sola vez a la funcion si se tomase como lugar inicial una celda "fuera" del
                                                             # tablero como (0,-1); pero me parece mas "realista"/claro de esta manera

        self.historial_movimientos.apilar({"Coordenadas":set(self.coordenadas_cambiadas), "Color":color_actual})
        print(f"DEBUG: {self.coordenadas_cambiadas}")
        print(f"{self.historial_movimientos.ver_tope()}")
        self.coordenadas_cambiadas = [ (0,0) ]


        """
        Asigna el nuevo color al Flood de la grilla. Es decir, a todas las
        coordenadas que formen un camino continuo del mismo color comenzando
        desde la coordenada origen en (0, 0) se les asignará `color_nuevo`

        Argumentos:
            color_nuevo: Valor del nuevo color a asignar al Flood.
        """
        # Parte 2: Tu código acá...


    def clonar(self):
        """
        Devuelve:
            Flood: Copia del Flood actual
        """
        # Parte 3: Tu código acá...
        return None


    def esta_completado(self):
        """
        Indica si todas las coordenadas de grilla tienen el mismo color

        Devuelve:
            bool: True si toda la grilla tiene el mismo color
        """
        # Parte 4: Tu código acá...
        return False
