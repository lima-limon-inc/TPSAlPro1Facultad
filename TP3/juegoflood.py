from flood import Flood
from pila import Pila
from cola import Cola


class JuegoFlood:
    """
    Clase para administrar un Flood, junto con sus estados y acciones
    """

    def __init__(self, alto, ancho, n_colores):
        """
        Genera un nuevo JuegoFlood, el cual tiene un Flood y otros
        atributos para realizar las distintas acciones del juego.

        Argumentos:
            alto, ancho (int): Tamaño de la grilla del Flood.
            n_colores: Cantidad maxima de colores a incluir en la grilla.
        """
        self.flood = Flood(alto, ancho)
        self.n_colores = n_colores
        self.flood.mezclar_tablero(n_colores)
        self.n_movimientos = 0
        self.pasos_solucion = Cola()
        self.mejor_n_movimientos, _ = self._calcular_movimientos()

    def cambiar_color(self, color):
        """
        Realiza la acción para seleccionar un color en el Flood, sumando a la
        cantidad de movimientos realizados y manejando las estructuras para
        deshacer y rehacer

        Argumentos:
            color (int): Nuevo color a seleccionar
        """
        if self.flood.cambiar_color(color) == 0: #Si ninguna celda fue cambiada, no queremos que 'cuente' como una accion
            return

        self.n_movimientos += 1
        self.flood.pila_rehacer = Pila() #Si el usuario selecciona un espacio nuevo, pierde la posibilidad de rehacer

        if not self.pasos_solucion.esta_vacia() and self.pasos_solucion.ver_frente() == color:
            self.pasos_solucion.desencolar()
        else:
            self.pasos_solucion = Cola()

    def deshacer(self):
        """
        Deshace el ultimo movimiento realizado si existen pasos previos,
        manejando las estructuras para deshacer y rehacer.
        """
        # Parte 3: cambiar el `return` por tu código...

        if self.flood.pila_deshacer.esta_vacia(): #Si no hay nada en la pila de rehacer, lo ignoramos
            return

        paso_anterior = self.flood.pila_deshacer.desapilar() #Nos guardamos los valores para la pila de rehacer

        self.flood.pila_rehacer.apilar({"Coordenadas":paso_anterior["Coordenadas"], "Color":self.flood.obtener_color(0,0)}) #Este diccionario representa las celdas con el color antes de que el usuario las cambie. Las coordenadas son las mismas que las de rehacer, lo unico que cambia es el color

        for coordenada in paso_anterior["Coordenadas"]:
            self.flood.tablero[coordenada] = paso_anterior["Color"]

        self.n_movimientos -= 1
        self.pasos_solucion = Cola()


    def rehacer(self):
        """
        Rehace el movimiento que fue deshecho si existe, manejando las
        estructuras para deshacer y rehacer.
        """
        # Parte 3: cambiar el `return` por tu código...
        if self.flood.pila_rehacer.esta_vacia():
            return

        paso_siguiente = self.flood.pila_rehacer.desapilar()

        self.flood.pila_deshacer.apilar({"Coordenadas":paso_siguiente["Coordenadas"], "Color":self.flood.obtener_color(0,0)}) #Este diccionario representa las celdas con el color al que habian sido cambiadas por el usuario. Las coordenadas son las mismas que las de rehacer, lo unico que cambia es el color


        for coordenada in paso_siguiente["Coordenadas"]:
            self.flood.tablero[coordenada] = paso_siguiente["Color"]

        self.n_movimientos += 1
        self.pasos_solucion = Cola()

    def _calcular_movimientos(self):
        '''
        Para el algoritmo de calcular los movimientos decidi usar la heuristica de: "El color que más casilleros agregaría al flood actua". Para lograr esto, cambio el color del flood a cada uno de los colores disponibles, guardando cuantas celdas anadiria cada uno (despues de cada paso deshago el cambio para volver al estado a evaluar). Una vez hecho eso efectuo el color que implique la mayor cantidad de celdas.
        Dicho proceso es repetido hasta que el tablero este completo.
        '''
        self.flood.pila_rehacer = Pila() #Reseteamos las pilas para que no generen problemas a la hora de buscar la solucion optima
        self.flood.pila_deshacer = Pila()

        sucesion_de_pasos = Cola()
        pasos_enlistados = []
        casillas_por_paso = {}
        while not self.flood.esta_completado():
            for i in range(self.n_colores): #Vamos a probar cada uno de los colores para ver cual es el que suma la mayor area.
                if len(pasos_enlistados) > 0 and i == pasos_enlistados[-1]: #No puede haber dos pasos con el mismo numero, este if lo evita
                    continue
                self.cambiar_color(i) # i representa el color
                tamano = self.flood.chequear_tamano_flood() #Vemos el tamano que produjo dicho cambio
                casillas_por_paso[i] = tamano
                self.deshacer()#Deshacemos para volver al estado anterior

            mayor_crecimiento = (-1, 0)

            for i in range(self.n_colores):
                if casillas_por_paso[i] > mayor_crecimiento[1]:
                    mayor_crecimiento = (i, casillas_por_paso[i])

            pasos_enlistados.append(mayor_crecimiento[0])
            ultimo_valor = pasos_enlistados[-1]
            self.cambiar_color(ultimo_valor)

        cantidad_de_pasos = len(pasos_enlistados)

        for valor in pasos_enlistados:
            sucesion_de_pasos.encolar(valor)

        while not self.flood.pila_deshacer.esta_vacia():
            self.deshacer()

        self.flood.pila_rehacer = Pila() #Volvemos a resetear las pilas para que el usuario no pueda acceder a las rtas
        self.flood.pila_deshacer = Pila()

        return cantidad_de_pasos, sucesion_de_pasos


    def hay_proximo_paso(self):
        """
        Devuelve un booleano indicando si hay una solución calculada
        """
        return not self.pasos_solucion.esta_vacia()


    def proximo_paso(self):
        """
        Si hay una solución calculada, devuelve el próximo paso.
        Caso contrario devuelve ValueError

        Devuelve:
            Color del próximo paso de la solución
        """
        return self.pasos_solucion.ver_frente()


    def calcular_nueva_solucion(self):
        """
        Calcula una secuencia de pasos que solucionan el estado actual
        del flood, de tal forma que se pueda llamar al método `proximo_paso()`
        """
        _, self.pasos_solucion = self._calcular_movimientos()

    def dimensiones(self):
        return self.flood.dimensiones()

    def obtener_color(self, col, fil):
        return self.flood.obtener_color(col, fil)

    def obtener_posibles_colores(self):
        return self.flood.obtener_posibles_colores()

    def esta_completado(self):
        return self.flood.esta_completado()
