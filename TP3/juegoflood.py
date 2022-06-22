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

        if self.flood.cambiar_color(color) == 0:
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
       #sucesion_de_pasos = Cola()
        sucesion_de_pasos = []
        casillas_por_paso = {}
       #while not self.flood.esta_completado():
        for i in range(self.n_colores):
            
            self.cambiar_color(i)
            tamano = self.flood.chequear_tamano_flood()
            casillas_por_paso[i] = tamano
            self.deshacer()
            print(i)
            print(tamano)
            input()

        mayor_crecimiento = (-1, 0)

        for i in range(len(casillas_por_paso)):
            if casillas_por_paso[i] > mayor_crecimiento[1]:
                mayor_crecimiento = (i, casillas_por_paso[i])

        sucesion_de_pasos.append(mayor_crecimiento[0])
        self.cambiar_color(sucesion_de_pasos[-1])

        print(sucesion_de_pasos)

        for i in range(self.n_colores):
            if i == self.cambiar_color(sucesion_de_pasos[-1]):
                pass
            self.cambiar_color(i)
            tamano = self.flood.chequear_tamano_flood()
            casillas_por_paso[i] = tamano
            self.deshacer()
            print(i)
            print(tamano)
            input()

        mayor_crecimiento = (-1, 0)

        for i in range(len(casillas_por_paso)):
            if casillas_por_paso[i] > mayor_crecimiento[1]:
                mayor_crecimiento = (i, casillas_por_paso[i])

        sucesion_de_pasos.append(mayor_crecimiento[0])
        self.cambiar_color(sucesion_de_pasos[-1])

        print(sucesion_de_pasos)








        """
        Realiza una solución de pasos contra el Flood actual (en una Cola)
        y devuelve la cantidad de movimientos que llevó a esa solución.

        COMPLETAR CON EL CRITERIO DEL ALGORITMO DE SOLUCIÓN.

        Devuelve:
            int: Cantidad de movimientos que llevó a la solución encontrada.
            Cola: Pasos utilizados para llegar a dicha solución
        """
        # Parte 4: tu código acá...
        return len(sucesion_de_pasos), Cola()
        return 999, Cola()


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
