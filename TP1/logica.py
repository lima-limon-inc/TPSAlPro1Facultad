# Imports
from random import choice

# Constantes globales 
## Constantes globales relacionada a la matriz
NUMERO_COLU  = 8
NUMERO_FILA  = 3 
ULTIMA_COLU  = NUMERO_COLU - 1
ULTIMA_FILA  = NUMERO_FILA - 1

## Constantes relacionadas a los controles
CONTROLES    = ("w","s","a","d") #1ero: Arriba; 2do:Abajo; 3ro: Izquierda; 4to: Derecha
MOV_ARRIBA   = CONTROLES[0]
MOV_ABAJO    = CONTROLES[1]
MOV_IZQUIERDA= CONTROLES[2]
MOV_DERECHA  = CONTROLES[3]
SALIR_JUEGO  = "o"

ESPACIO_VACIO = "E"

# Funciones
def generar_matriz():
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
    
    for fila in range(NUMERO_FILA):
        matriz.append([])
        for columna in range(NUMERO_COLU):
            matriz[fila].append(valor_celda)
            valor_celda += 1

    matriz[-1][-1] = "E"
    vacio_fila = ULTIMA_FILA
    vacio_colu = ULTIMA_COLU

    return matriz, vacio_fila, vacio_colu

def generador_de_movs(cantidad_de_movs):
    matriz, vacio_fila, vacio_colu = generar_matriz() 
    
    movidas_realizadas = []

    for i in range(cantidad_de_movs):
        jugada_a_realizar = choice(CONTROLES)
        while es_movimiento_valido(jugada_a_realizar,vacio_fila, vacio_colu) == False:
            jugada_a_realizar = choice(CONTROLES)
        DEBUG,vacio_fila, vacio_colu, matriz, DEBUG2 =  mover_vacio(jugada_a_realizar, (vacio_fila, vacio_colu), matriz, [])
        movidas_realizadas.append(jugada_a_realizar)
    print(movidas_realizadas)

    for i in range(len(matriz)): #TODO: hacer que esto quede mas lindo
        print(matriz[i])

def mostrar_juego(matriz,historial_movimeintos):
    for i in range(4):
        print()

    print(f"=== Fifteen ===")      

    for i in range(len(matriz)): #TODO: hacer que esto quede mas lindo
        print(matriz[i])

    print(f"Controles Arriba:{MOV_ARRIBA}, Abajo:{MOV_ABAJO}, Izquierda:{MOV_IZQUIERDA}, Derecha:{MOV_DERECHA}")
    print(f"Salir del juego: {SALIR_JUEGO} ")
    print("Cantidad de movimientos: " + str(len(historial_movimeintos)))


def mover_vacio(movimientos, coord_vacio, matriz, historial_movimientos): #Movimientos es una lista
    vacio_fila = coord_vacio[0]
    vacio_colu = coord_vacio[1]

    for movimiento in movimientos:
        movimientos = movimientos[1:] #Apenas un movimiento es procesado quiero sacarlo de la "lista" de movimientos


       #print("DEBUG CHEQUER OUTPUT: " + str(es_movimiento_valido(movimiento,vacio_fila, vacio_colu)))
        if es_movimiento_valido(movimiento, vacio_fila, vacio_colu) == False:
            break

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
        
    return movimientos, vacio_fila, vacio_colu ,matriz, historial_movimientos



def es_movimiento_valido(mov_a_chequear, vacio_fila, vacio_colu):
    '''
    Funcion que dada un movimiento y una matriz, devuelve un booleano que determina si el movimiento es valido o invalido
    '''

    print(f"DEBUG CHEQUEAR MOVIMIENTO {mov_a_chequear}")

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
generador_de_movs(20)
