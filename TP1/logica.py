# Imports
from random import randint

# Constantes globales
MATRIZ_COLUMNAS = 6
MATRIZ_FILAS    = 3 
ESPACIO_VACIO   = "E"

# Funciones
def generar_matriz():
    '''
    Funcion que genera una matriz de NxM dimensiones, dependiendo de las constantes globales MATRIZ_FILAS & MATRIZ_COLUMNAS
    ejemplo de Matriz 3x3
    [
    [a,b,c],
    [d,e,f],
    [g,h,i]
    ]
    '''
    matriz = [] 
    valor_celda = 1
    
    for fila in range(MATRIZ_FILAS):
        matriz.append([])
        for columna in range(MATRIZ_COLUMNAS):
            matriz[fila].append(valor_celda)
            valor_celda += 1

    matriz[-1][-1] = "E"
    
    return matriz

def mover_vacio(movimientos): #Movimientos es una lista
    '''
    Funcion que, dada una matriz, aleatoriza todas las posiciones #TODO: CAMBIAR COMENTARIO
    '''

    matriz = generar_matriz() #TODO: Cambiar nombre
    for i in range(len(matriz)):
        print(matriz[i])  
    
    print()
    coord_vacio = [MATRIZ_FILAS - 1, MATRIZ_COLUMNAS - 1] #TODO: BORRAR coord_vacio[0] = Fila; #coord_vacio[1] = Columna
    vacio_fila = coord_vacio[0]
    vacio_colu = coord_vacio[1]
    print(coord_vacio)
    print()


    for movimiento in movimientos:
        if movimiento == "Abajo":  
            if vacio_fila != 0: #Ejecuta lo de abajo si y solo si el espacio vacio no esta en la fila 0.

                matriz[vacio_fila][vacio_colu],matriz[vacio_fila - 1][vacio_colu] = matriz[vacio_fila - 1][vacio_colu],matriz[vacio_fila][vacio_colu]
                vacio_fila = vacio_fila - 1

        if movimiento == "Arriba": #Ejecuta lo de abajo si y solo si el espacio vacio no esta en la ultima fila.
            if vacio_fila != MATRIZ_FILAS - 1: 

                matriz[vacio_fila][vacio_colu],matriz[vacio_fila + 1][vacio_colu] = matriz[vacio_fila + 1][vacio_colu],matriz[vacio_fila][vacio_colu]
                vacio_fila = vacio_fila + 1

        if movimiento == "Derecha" :#Ejecuta lo de abajo si y solo si el espacio vacio no esta en la primera columna
            if vacio_colu != 0:

                matriz[vacio_fila][vacio_colu],matriz[vacio_fila][vacio_colu - 1] = matriz[vacio_fila][vacio_colu - 1],matriz[vacio_fila][vacio_colu]
                vacio_colu = vacio_colu - 1

        if movimiento == "Izquierda" :#Ejecuta lo de abajo si y solo si el espacio vacio no esta en la ultima columna
            if vacio_colu != MATRIZ_COLUMNAS - 1:

                matriz[vacio_fila][vacio_colu],matriz[vacio_fila][vacio_colu + 1] = matriz[vacio_fila][vacio_colu + 1],matriz[vacio_fila][vacio_colu]
                # a,b = b,a
                vacio_colu = vacio_colu + 1
       

    print()
    print(coord_vacio)
    print()

    for i in range(len(matriz)):
        print(matriz[i])     

# Funciones debug BORRAR DESPUES
mover_vacio(["Arriba","Arriba","Arriba","Arriba","Arriba","Arriba","Arriba","Arriba","Arriba","Arriba","Arriba",])
#print(generar_cantidad_cuadrados())

# Funcion para que queda linda la matriz, anadir ljust y rjust
#for i in range(len(matriz)):
#        print(matriz[i])
    
# input 
