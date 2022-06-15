import random


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



    def obtener_color(self, fil, col):
        """
        Devuelve el color que se encuentra en las coordenadas solicitadas.

        Argumentos:
            fil, col (int): Posiciones de la fila y columna en la grilla.

        Devuelve:
            Color asignado.
        """
        # Parte 1: Cambiar el `raise` por tu código...
        return self.tablero[(col,fil)]


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


    def moverse(self):
        '''
        Si vengo de la derecha, no tengo que chequear la izquierda. Si vengo de arriba, no tengo que chequear abajo
        '''
        for i in range(3) #Son 3 direcciones posibles
    

    def cambiar_color(self, color_nuevo):

        coordenadas_visitadas = set()
        color_actual = self.obtener_posibles_colores(0,0)



        """
        Asigna el nuevo color al Flood de la grilla. Es decir, a todas las
        coordenadas que formen un camino continuo del mismo color comenzando
        desde la coordenada origen en (0, 0) se les asignará `color_nuevo`

        Argumentos:
            color_nuevo: Valor del nuevo color a asignar al Flood.
        """
        # Parte 2: Tu código acá...
        return


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
