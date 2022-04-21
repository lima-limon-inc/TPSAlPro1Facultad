# Imports
from random import randint

# Constantes globales
MATRIZ_COLUMNAS = 4  
MATRIZ_FILAS    = 4 
ESPACIO_VACIO   = "E"

# Funciones
def generar_cantidad_cuadrados():
    '''
    Funcion que genera una lista de numeros, dependiendo de la cantidad de filas y columnas
    La formula para hallar esto es (MATRIZ_FILAS x MATRIZ_COLUMNAS) - 1
    '''
    cantidad_de_cuadrados = MATRIZ_COLUMNAS * MATRIZ_FILAS
    lista_con_cuadrados = []

    for i in range(1,cantidad_de_cuadrados): #Arranca desde 1 porque el 0 no es usado en el juego
        lista_con_cuadrados.append(i)
    lista_con_cuadrados.append(ESPACIO_VACIO)

    return lista_con_cuadrados
    
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
    cuadrados = generar_cantidad_cuadrados()

    for fila in range(MATRIZ_FILAS):
        matriz.append([])
        for columna in range(MATRIZ_COLUMNAS):
            matriz[fila].append(cuadrados[columna])

        for cuadrado in range(MATRIZ_COLUMNAS):
            cuadrados.pop(0)
    
    return matriz

def mover_vacio(movimientos): #Movimientos es una lista
    '''
    Funcion que, dada una matriz, aleatoriza todas las posiciones
    '''

    matriz = generar_matriz() #TODO: Cambiar nombre
    for i in range(len(matriz)):
        print(matriz[i])  
    
    print()
    coord_vacio = [MATRIZ_FILAS - 1, MATRIZ_COLUMNAS - 1] #TODO: BORRAR coord_vacio[0] = Fila; #coord_vacio[1] = Columna
    print(coord_vacio)
    print()


    for movimiento in movimientos:
        if movimiento == "Abajo":  
            #Ejecuta lo de abajo si y solo si el vacio no esta arriba de todo (esto mismo aplica para los otros 4)
            if coord_vacio[0] != 0: 
                #Coordenada del vacio en matriz        Coordenada de misma columna, 1 fila arriba   
                matriz[coord_vacio[0]][coord_vacio[1]],matriz[coord_vacio[0] - 1][coord_vacio[1]] = matriz[coord_vacio[0] - 1][coord_vacio[1]],matriz[coord_vacio[0]][coord_vacio[1]]
                coord_vacio[0] = coord_vacio[0] - 1

        if movimiento == "Derecha":
            if coord_vacio[1] != 0:
                #Coordenada del vacio en matriz        Coordenada de misma columna, 1 column  izq
                matriz[coord_vacio[0]][coord_vacio[1]],matriz[coord_vacio[0]][coord_vacio[1] - 1] = matriz[coord_vacio[0]][coord_vacio[1] - 1],matriz[coord_vacio[0]][coord_vacio[1]]
                coord_vacio[1] = coord_vacio[1] - 1

        if movimiento == "Arriba": 
            if coord_vacio[0] != MATRIZ_FILAS - 1: 
                #Coordenada del vacio en matriz        Coordenada de misma columna, 1 fila abajo   
                matriz[coord_vacio[0]][coord_vacio[1]],matriz[coord_vacio[0] + 1][coord_vacio[1]] = matriz[coord_vacio[0] + 1][coord_vacio[1]],matriz[coord_vacio[0]][coord_vacio[1]]
                coord_vacio[0] = coord_vacio[0] + 1

        if movimiento == "Izquierda":
            if coord_vacio[1] != MATRIZ_COLUMNAS - 1:
                #Coordenada del vacio en matriz        Coordenada de misma columna, 1 column der
                matriz[coord_vacio[0]][coord_vacio[1]],matriz[coord_vacio[0]][coord_vacio[1] + 1] = matriz[coord_vacio[0]][coord_vacio[1] + 1],matriz[coord_vacio[0]][coord_vacio[1]]
                coord_vacio[1] = coord_vacio[1] + 1
       

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
