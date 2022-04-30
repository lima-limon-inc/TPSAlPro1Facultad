# Imports
from random import choice, randint

# Constantes globales 
## Constantes globales relacionada a la matriz
NUMERO_COLU  = 21
NUMERO_FILA  = 10
ULTIMA_COLU  = NUMERO_COLU - 1
ULTIMA_FILA  = NUMERO_FILA - 1
CUANTO_MEZCLAR  = 10#randint(25,50)

## Constantes relacionadas a los controles
CONTROLES    = ("w","s","a","d") #1ero: Arriba; 2do:Abajo; 3ro: Izquierda; 4to: Derecha
MOV_ARRIBA   = CONTROLES[0]
MOV_ABAJO    = CONTROLES[1]
MOV_IZQUIERDA= CONTROLES[2]
MOV_DERECHA  = CONTROLES[3]
SALIR_JUEGO  = "o"

ESPACIO_VACIO = " "

# Funciones
def generar_matriz(filas, columnas):
    '''
    Funcion que genera una matriz de NxM dimensiones, dependiendo de las constantes globales NUMERO_FILA & NUMERO_COLU
    Ejemplo de como se deberia ver una matriz 3x3
    [
    [a,b,c],
    [d,e,f],
    [g,h,i]
    ]
    '''
    matriz = [] 
    valor_celda = 1
    
    for fila in range(filas):
        matriz.append([])
        for columna in range(columnas):
            matriz[fila].append(valor_celda)
            valor_celda += 1

    matriz[-1][-1] = ESPACIO_VACIO
    vacio_fila = ULTIMA_FILA
    vacio_colu = ULTIMA_COLU

    return matriz, vacio_fila, vacio_colu

def generar_tablero(filas, columnas, cuanto_mezclar):
    
    matriz, vacio_fila, vacio_colu = generar_matriz(filas,columnas)

    historial_movimientos = []

    for i in range(cuanto_mezclar):
        jugada_a_realizar = choice(CONTROLES)

        while es_movimiento_valido(jugada_a_realizar,vacio_fila, vacio_colu) == False:
            jugada_a_realizar = choice(CONTROLES)

        vacio_fila, vacio_colu, matriz, historial_movimientos =  mover_vacio(jugada_a_realizar, vacio_fila, vacio_colu, matriz, historial_movimientos)

    print(f"DEBUG MOVS: {historial_movimientos}") #DEBUG

    return matriz, vacio_fila, vacio_colu, historial_movimientos

def mostrar_juego(matriz,historial_movimeintos):
    for i in range(4):
        print()
    
    espaciado = len(matriz[0]) #- len(" Fifteen ")
    print("=" * espaciado  + " Fifteen " +  "=" * espaciado)      

    for i in range(len(matriz)): #TODO: hacer que esto quede mas lindo
        for j in range(len(matriz[i])):
            if j == len(matriz[i]) - 1:
                ending = "\n"
            else:
                ending = " | "
            print(str(matriz[i][j]).center(len(str((NUMERO_FILA * NUMERO_COLU) - 1))), end=ending) #len(str((NUMERO_FILA * NUMERO_COLU) - 1)) Esta funcion calcula la longitud del digito que el espacio reemplaza. Esto asegura que el tablero va a estar ordenado, sin importar el numero de filas y columnas (ignorando el monitor)
    

    print(f"Controles Arriba:{MOV_ARRIBA}, Abajo:{MOV_ABAJO}, Izquierda:{MOV_IZQUIERDA}, Derecha:{MOV_DERECHA}")
    print(f"Salir del juego: {SALIR_JUEGO} ")
    print("Cantidad de movimientos: " + str(len(historial_movimeintos)))

def mover_vacio(movimientos, vacio_fila, vacio_colu, matriz, historial_movimientos): #Movimientos es una lista
    for movimiento in movimientos:
        while es_movimiento_valido(movimiento, vacio_fila, vacio_colu) == False:
            movimiento = input(f"{movimiento} es invalido: ")

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
        historial_movimientos.append(movimiento) 

    return vacio_fila, vacio_colu ,matriz, historial_movimientos

def es_movimiento_valido(mov_a_chequear, vacio_fila, vacio_colu):
    '''
    Funcion que dada un movimiento y una matriz, devuelve un booleano que determina si el movimiento es valido o invalido
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
