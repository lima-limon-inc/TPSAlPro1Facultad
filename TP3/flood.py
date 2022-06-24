import random
from pila import Pila

DIRECCIONES = {             #Conjunto que representa las direcciones a las que una celda puede ser adyacente. USandfo cuando se calcula a que celda ir siguiente. Se toma como (0,0) la esquina izquierda superior, de ahi que bajar aumenta las "y" y subir las resta; y que ir a la derecha aumenta las "x" e ir a la izquierda las disminuye
        (0,1), #Abajo
        (0,-1),#Arriba
        (1,0), #Derecha
        (-1,0),#Izquierda
        }

class Flood:
    """
    Clase para administrar un tablero de N colores.
    """

    def __init__(self, alto, ancho):
        self.alto = alto    #Me guardo el tamano del flood por separado
        self.ancho = ancho
        """
        Genera un nuevo Flood de un mismo color con las dimensiones dadas.

        Argumentos:
            alto, ancho (int): Tamaño de la grilla.
        """
        self.tablero = {} #Creo el diccionario que voy a usar como tablero

        for y in range(self.alto):
            for x in range(self.ancho):
                self.tablero[x,y] = 0 #Anado todos los valores (empiezan todos pintados de 0)


        self.coordenadas_cambiadas = { (0,0) } #Representa las coordenadas que son cambiadas cuando se llama a .cambiar_color()
        self.coordenadas_visitadas = { (0,0) } #Representa las coordenadas que son visitadas cuando se llama a chequear_tamano_flood()

        self.pila_deshacer = Pila()
        self.pila_rehacer = Pila()
    def mezclar_tablero(self, n_colores):
        """
        Asigna de forma completamente aleatoria hasta `n_colores` a lo largo de
        las casillas del tablero.

        Argumentos:
            n_colores (int): Cantidad maxima de colores a incluir en la grilla.
        """
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
        return [i for i in range(self.n_colores)]

    def dimensiones(self):
        """
        Dimensiones de la grilla (filas y columnas)

        Devuelve:
            (int, int): alto y ancho de la grilla en ese orden.
        """
        return self.alto, self.ancho

    def _cambiar_color(self, desde, hasta, color_actual, color_nuevo):
        if self.obtener_color(hasta[0], hasta[1]) != color_actual: #Si la celda a la que llegamos tiene un color diferente a color_actual, significa que no es parte del flood, asique no nos interesa
            return

        self.tablero[hasta] = color_nuevo     #En este paso se pinta la celda al nuevo color
        self.coordenadas_cambiadas.add(hasta) #Dicha celda se guarda, para luego ser almacenada en la pila de deshacer

        de_donde_vengo = {(-1 * abs(desde[0] - hasta[0]), -1 * abs(desde[1] - hasta[1]))} #Esto calcula cual fue la celda que nos trajo a la celda en la que estamos, dicha celda ya fue pintada, asique no hace falta ir hacia ella

        a_donde_voy = DIRECCIONES - de_donde_vengo #La interseccion entre estos dos conjuntos nos da las 3 direcciones a las que tenemos que ir a continuacion

        for tupla in a_donde_voy:
            self._cambiar_color(hasta, ((hasta[0] + tupla[0]), (hasta[1] + tupla[1])), color_actual, color_nuevo) #Llamada recursiva hacia las 3 celdas que tenemos que ir (la celda a la que no vamos es la celda de donde vinimos)


        '''
        Si vengo de la derecha, no tengo que chequear la izquierda. Si vengo de arriba, no tengo que chequear abajo
        '''
    def cambiar_color(self, color_nuevo):
        color_actual = self.obtener_color(0,0) #Guardamos el valor de la celda (0,0) antes de pintarla
        if color_actual == color_nuevo: #Si el color nuevo es igual al actual, entonces no hay nada que cambiar. En esos casos devolvemos "Ignorar" --> "Los salteamos" (No se devuelve None, ya que genera conflictos con la funcion main.py de Diego)
            return None

        self.tablero[(0, 0)] = color_nuevo #Pintamos la primera coordenada por separado, ya que la recursion empieza desde la primera y va a las siguientes celdas
        self._cambiar_color((0,0),(1,0), color_actual, color_nuevo) # La funcion _cambiar_color toma como parametro la celda de partida, por eso es llamada dos veces (ya que (0,0) tiene dos celdas adyacentes, las cuales son
        self._cambiar_color((0,0),(0,1), color_actual, color_nuevo) # las que le van a dar comienzo a la recursion. Se podria llamar una sola vez a la funcion si se tomase como lugar inicial una celda "fuera" del
                                                                    # tablero como (0,-1); pero me parece mas "realista"/claro de esta manera

        self.pila_deshacer.apilar({"Coordenadas":self.coordenadas_cambiadas, "Color":color_actual}) #En la pila de deshacer, guardamos todas las celdas que fueron cambiadas de color con el color que tenian previamente; en vez de una copia de todo el tablero.

        cantidad_coordenadas_cambiadas = len(self.coordenadas_cambiadas)

        self.coordenadas_cambiadas = { (0,0) } #Reseteamos los valores cambiados, como (0,0) lo cambiamos fuera de la recursion por lo explicado previamente, ya lo guardamos para la proxima recursion
        
        return cantidad_coordenadas_cambiadas
        """
        Asigna el nuevo color al Flood de la grilla. Es decir, a todas las
        coordenadas que formen un camino continuo del mismo color comenzando
        desde la coordenada origen en (0, 0) se les asignará `color_nuevo`

        Argumentos:
            color_nuevo: Valor del nuevo color a asignar al Flood.
        """
        # Parte 2: Tu código acá...

    def _chequear_tamano_flood(self, desde, hasta, color):
        if self.obtener_color(hasta[0], hasta[1]) != color or hasta in self.coordenadas_visitadas: #Ignoramos las celdas ya visitadas o que tienen otro color al color que pasamos
            return

        self.coordenadas_visitadas.add(hasta) #Lo anadimos a las coordenadas visitadas

        de_donde_vengo = {(-1 * abs(desde[0] - hasta[0]), -1 * abs(desde[1] - hasta[1]))} #Esto calculo cual fue la celda que nos trajo a la celda en la que estamos, dicha celda ya fue pintada, asique no hace falta ir hacia ella

        a_donde_voy = DIRECCIONES - de_donde_vengo #La interseccion entre estos dos conjuntos nos da las 3 direcciones a las que tenemos que ir a continuacion

        for tupla in a_donde_voy:
            self._chequear_tamano_flood(hasta, ((hasta[0] + tupla[0]), (hasta[1] + tupla[1])), color)
        '''
        Si vengo de la derecha, no tengo que chequear la izquierda. Si vengo de arriba, no tengo que chequear abajo
        '''

    def chequear_tamano_flood(self):
        color = self.obtener_color(0,0)

        self._chequear_tamano_flood((0,0),(1,0), color) # La funcion _cambiar_color toma como parametro la celda de partida, por eso es llamada dos veces (ya que (0,0) tiene dos celdas adyacentes, las cuales son
        self._chequear_tamano_flood((0,0),(0,1), color) # las que le van a dar comienzo a la recursion. Se podria llamar una sola vez a la funcion si se tomase como lugar inicial una celda "fuera" del

        tamano = len(self.coordenadas_visitadas)
        self.coordenadas_visitadas = { (0,0) }

        return tamano

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

        color_actual = self.obtener_color(0,0)

        for x in range(self.dimensiones()[1] - 1, -1, -1):                #Como el tablero va evoluciando de la esquina de arriba a la izquierda hacia el resto del tablero;
            for y in range(self.dimensiones()[0] - 1, -1, -1):            #empezamos a chequear desde la esquina de abajo a la derecha, ya que es mas probable encontrar uno diferente desde ahi.
                if self.obtener_color(x,y) != self.obtener_color(0,0):    #Solo hace falta chequear que sean iguales al 0,0; si son diferentes, significa que el tablero no es de un solo color.
                    return False
        return True
