# Imports
from random import choice, randint

# Constantes globales 
## Constantes globales relacionada a la matriz
NUMERO_COLU  = 4
NUMERO_FILA  = 4
ULTIMA_COLU  = NUMERO_COLU - 1
ULTIMA_FILA  = NUMERO_FILA - 1
CUANTO_MEZCLAR  = NUMERO_FILA * NUMERO_COLU * 2

## Constantes relacionadas a los controles
CONTROLES    = ("w","s","a","d") #1ero: Arriba; 2do:Abajo; 3ro: Izquierda; 4to: Derecha
MOV_ARRIBA   = CONTROLES[0]
MOV_ABAJO    = CONTROLES[1]
MOV_IZQUIERDA= CONTROLES[2]
MOV_DERECHA  = CONTROLES[3]
SALIR_JUEGO  = "o"

## Constantes relacionadas al display del juego
ESPACIO_VACIO = " "

# Funciones
def generar_matriz(filas, columnas):
    '''
    Funcion que genera una matriz con todos los numeros hasta el NUMERO_COLU * NUMERO_FILA (excepto en la ultima, donde esta el ESPACIO_VACIO)
    Recibe:
        0. filas -> int. Cantidad de filas que se quiere que tenga el tablero.
        1. columnas -> int. Cantidad de columnas que se quiere que tenga el tablero.
    Devuelve: 
        0. matriz -> list. Matriz de filas X columnas 
        1. vacio_fila -> int. Representa la fila donde el espacio vacio esta
        2. vacio_colu -> int. Representa la columnda donde el espacio vacio esta 
    '''
    matriz = [] 
    valor_celda = 1
    
    for fila in range(filas):
        matriz.append([])
        for columna in range(columnas):
            matriz[fila].append(valor_celda)
            valor_celda += 1

    matriz[-1][-1] = ESPACIO_VACIO #Siempre quiero que el espacio blanco sea el ultimo
    vacio_fila = ULTIMA_FILA
    vacio_colu = ULTIMA_COLU

    return matriz, vacio_fila, vacio_colu

def generar_tablero(filas, columnas, cuanto_mezclar):
    '''
    Funcion que, dada una matriz con el espacio en blanco, mezcla todos los elementos una cantidad "cuanto_mezclar" de veces. 
    Recibe:
        0. filas -> int. Cantidad de filas que se quiere que tenga el tablero.
        1. columnas -> int. Cantidad de columnas que se quiere que tenga el tablero.
        2. cuanto_mezclar -> int. Cantidad de veces que se quiere que se mueva el espacio en blanco para mezclar el tablero
    Devuelve:
        0. matriz -> list. Matriz de filas X columnas 
        1. vacio_fila -> int. Representa la fila donde el espacio vacio esta
        2. vacio_colu -> int. Representa la columnda donde el espacio vacio esta 
        3. historial_movimientos -> list. Lista donde se almacenan todos los movimientos realizados (incluyendo los que se hacen al principio para aleatorizar el tablero)
    '''
    matriz, vacio_fila, vacio_colu = generar_matriz(filas,columnas)

    historial_movimientos = []

    for i in range(cuanto_mezclar):
        jugada_a_realizar = choice(CONTROLES)

        while es_movimiento_valido(jugada_a_realizar,vacio_fila, vacio_colu) == False: #No va a salir de este while loop  hasta que un movimiento valido sea aleatoriamente elegido
            jugada_a_realizar = choice(CONTROLES)

        matriz,vacio_fila, vacio_colu,  historial_movimientos =  mover_vacio(jugada_a_realizar, matriz, vacio_fila, vacio_colu, historial_movimientos) # Apenas se genere un movimiento valido, se realiza y se guarda

    return matriz, vacio_fila, vacio_colu, historial_movimientos

def mostrar_juego(matriz,historial_movimeintos):
    '''
    Funcion que muestra el estado del juego (el tablero, cantidad de movimientos realizados y maxima cantidad de movimientos, nombre del juego 
    Recibe:
        0. matriz -> list. Matriz de filas X columnas 
        1. historial_movimientos -> list. Lista donde se almacenan todos los movimientos realizados (incluyendo los que se hacen al principio para aleatorizar el tablero)
    Devuelve:
        0. None
        Es una funcion impura, no devuelve "nada", solo tiene efectos secundarios.
    '''
    for i in range(4): #Crea un espacio inicial para separarlo de la linea anterior
        print()
    
    espaciado = len(str(matriz[0])) - len(" Fifteen ") # Int que representa la cantidad de "=" que tiene que haber despues y antes del titulo "Fifteen"
    print("=" * espaciado  + " Fifteen " +  "=" * espaciado)      

    for i in range(len(matriz)): #Funcion que le da formato con " | " y el espaciado
        for j in range(len(matriz[i])):
            if j == len(matriz[i]) - 1:
                ending = "\n"
            else:
                ending = " | "
            print(str(matriz[i][j]).center(len(str((NUMERO_FILA * NUMERO_COLU) - 1))), end=ending) # 'len(str((NUMERO_FILA * NUMERO_COLU) - 1))' Esta funcion calcula la longitud del digito mas grande. Esto deberia asegurar que el tablero va a estar ordenado y prolijo, sin importar el numero de filas y columnas (ignorando el monitor)
    

    print(f"Controles Arriba:{MOV_ARRIBA}, Abajo:{MOV_ABAJO}, Izquierda:{MOV_IZQUIERDA}, Derecha:{MOV_DERECHA}")
    print(f"Salir del juego: {SALIR_JUEGO} ")
    print("Cantidad de movimientos: " + str(len(historial_movimeintos) - CUANTO_MEZCLAR) + "/" + str(CUANTO_MEZCLAR * 5))

def mover_vacio(movimientos, matriz, vacio_fila, vacio_colu, historial_movimientos): #Movimientos es una lista
    '''
    Funcion que se encarga de mover el espacio en blanco. Todos los movimientos son anadidos a historial_movimientos
    Recibe:
        0. movimientos -> str. Cadena con todos los movimientos del usuario (del estilo: "adwddwc")
        1. matriz -> list. Matriz de filas X columnas 
        2. vacio_fila -> int. Representa la fila donde el espacio vacio esta
        3. vacio_colu -> int. Representa la columnda donde el espacio vacio esta 
        4. historial_movimientos -> list. Lista donde se almacenan todos los movimientos realizados (incluyendo los que se hacen al principio para aleatorizar el tablero)
    Devuelve:
        0. matriz -> list. Matriz de filas X columnas 
        1. vacio_fila -> int. Representa la fila donde el espacio vacio esta
        2. vacio_colu -> int. Representa la columnda donde el espacio vacio esta 
        3. historial_movimientos -> list. Lista donde se almacenan todos los movimientos realizados (incluyendo los que se hacen al principio para aleatorizar el tablero)
    '''
    movs_procesados = 0
    for movimiento in movimientos:
        while es_movimiento_valido(movimiento, vacio_fila, vacio_colu) == False:
            mostrar_juego(matriz, historial_movimientos)
            print(f"Tu entrada:{movimientos}")
            print(" " * (len("Tu entrada:") + movs_procesados) +  "^")
            movimiento = input(f"{movimiento} es invalido. Corregir: ")

        if movimiento == MOV_ABAJO:  
            matriz[vacio_fila][vacio_colu],matriz[vacio_fila - 1][vacio_colu] = matriz[vacio_fila - 1][vacio_colu],matriz[vacio_fila][vacio_colu]
            vacio_fila = vacio_fila - 1

        if movimiento == MOV_ARRIBA: #Ejecuta lo de abajo si y solo si el espacio vacio no esta en la ultima fila.
            matriz[vacio_fila][vacio_colu],matriz[vacio_fila + 1][vacio_colu] = matriz[vacio_fila + 1][vacio_colu],matriz[vacio_fila][vacio_colu]
            vacio_fila = vacio_fila + 1

        if movimiento == MOV_DERECHA:#Ejecuta lo de abajo si y solo si el espacio vacio no esta en la primera columna
            matriz[vacio_fila][vacio_colu],matriz[vacio_fila][vacio_colu - 1] = matriz[vacio_fila][vacio_colu - 1],matriz[vacio_fila][vacio_colu]
            vacio_colu = vacio_colu - 1

        if movimiento == MOV_IZQUIERDA :#Ejecuta lo de abajo si y solo si el espacio vacio no esta en la ultima columna
            matriz[vacio_fila][vacio_colu],matriz[vacio_fila][vacio_colu + 1] = matriz[vacio_fila][vacio_colu + 1],matriz[vacio_fila][vacio_colu]
            vacio_colu = vacio_colu + 1

        movs_procesados += 1
        historial_movimientos.append(movimiento) 

    return matriz, vacio_fila, vacio_colu, historial_movimientos

def es_movimiento_valido(mov_a_chequear, vacio_fila, vacio_colu):
    '''
    Funcion que dada un movimiento y una matriz, devuelve un booleano que determina si el movimiento es valido o invalido
    Recibe:
        0. mov_a_chequear -> str
        1. vacio_fila -> int. Representa la fila donde el espacio vacio esta
        2. vacio_colu -> int. Representa la columnda donde el espacio vacio esta 
    Devuelve:
        0. True/False -> bool. Dependiendo de si el movimiento es valido o no
    '''
    if mov_a_chequear not in CONTROLES:
        return False
    
    if mov_a_chequear == MOV_ABAJO and vacio_fila == 0: #Intenta moverse para abajo, pero como no hay fichas encima del vacio esto es invalido
        return False 

    if mov_a_chequear == MOV_ARRIBA and vacio_fila == ULTIMA_FILA:
        return False 

    if mov_a_chequear == MOV_DERECHA and vacio_colu == 0:
        return False 

    if mov_a_chequear == MOV_IZQUIERDA and vacio_colu == ULTIMA_COLU:
        return False 
    
    else:
        return True

def frase_motivadora():
    '''
    Funcion que contiene una lista con una serie de frases para motivar al usuario en caso de que pierda
    Recibe:
        0.Nada
    Devuelve:
        0.choice(lista_frases) -> str. Frase aleatoria dentro de la lista
    '''
    lista_frases = ["'Nada está perdido si se tiene el valor de proclamar que todo está perdido y hay que empezar de nuevo'.-Julio Cortázar", "'Llegará un momento en que creas que todo ha terminado. Ese será el principio.' -Epicuro","'El fracaso es la oportunidad de comenzar de nuevo con más inteligencia'.-Henry Ford"]

    return choice(lista_frases)

# PD: Sin contar la documentacion, son 135 lineas de codigo
