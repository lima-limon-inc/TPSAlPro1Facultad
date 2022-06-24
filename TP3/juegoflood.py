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
        self.mejor_n_movimientos, _ = self._calcular_movimientos()
        self.n_movimientos = 0
        self.pasos_solucion = Cola()

        # Parte 3: Agregar atributos a la clase...


    def cambiar_color(self, color):
        """
        Realiza la acción para seleccionar un color en el Flood, sumando a la
        cantidad de movimientos realizados y manejando las estructuras para
        deshacer y rehacer

        Argumentos:
            color (int): Nuevo color a seleccionar
        """
        # Parte 3: Modificar el código...

        if self.flood.cambiar_color(color) == "Ignorar":
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

        if self.flood.pila_deshacer.esta_vacia():
            return

        paso_anterior = self.flood.pila_deshacer.desapilar()

        self.flood.pila_rehacer.apilar({"Coordenadas":paso_anterior["Coordenadas"], "Color":self.flood.obtener_color(0,0)})

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

        self.flood.pila_deshacer.apilar({"Coordenadas":paso_siguiente["Coordenadas"], "Color":self.flood.obtener_color(0,0)})

        for coordenada in paso_siguiente["Coordenadas"]:
            self.flood.tablero[coordenada] = paso_siguiente["Color"]

        self.n_movimientos += 1
        self.pasos_solucion = Cola()

    def _calcular_movimientos(self):
       sucesion_de_pasos = Cola()
       casillas_por_paso = {}
       while not self.flood.esta_completado():
            for i in range(self.n_colores):  #Vamos a probar cada uno de los colores para ver cual es el que suma la mayor area.
                if sucesion_de_pasos.esta_vacia() and i == self.cambiar_color(sucesion_de_pasos[-1]): #No puede haber dos pasos con el mismo numero, este if lo evita
                    continue
                self.cambiar_color(i) # i representa el color
                tamano = self.flood.chequear_tamano_flood() #Vemos el tamano que produjo dicho cambio
                casillas_por_paso[i] = tamano
                self.deshacer() #Deshacemos para volver al estado anterior

            maximo_crecimiento = max(casillas_por_paso)

            sucesion_de_pasos.encolar(maximo_crecimiento)

            self.cambiar_color(maximo_crecimiento)


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
