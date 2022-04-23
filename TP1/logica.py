# Imports
from random import randint

# Constantes globales 
## Constantes globales relacionada a la matriz
NUMERO_COLU  = 6
NUMERO_FILA  = 3 
ULTIMA_COLU  = NUMERO_COLU - 1
ULTIMA_FILA  = NUMERO_FILA - 1

## Constantes controles
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
    ejemplo de Matriz 3x3
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

    return matriz

def mostrar_juego(matriz):
    for i in range(4):
        print()

    for i in range(len(matriz)): #TODO: hacer que esto quede mas lindo
        print(matriz[i])
    
    print(f"Controles Arriba:{MOV_ARRIBA}, Abajo:{MOV_ABAJO}, Izquierda:{MOV_IZQUIERDA}, Derecha:{MOV_DERECHA}")
    print(f"Salir del juego: {SALIR_JUEGO} ")


def mover_vacio(movimientos, coord_vacio, matriz): #Movimientos es una lista

    for movimiento in movimientos:
        if movimiento not in CONTROLES:
            print("DEBUG MOVIMIENTO INVALIDO")


        if movimiento == MOV_ABAJO:  
            if coord_vacio[0] != 0: #Ejecuta lo de abajo si y solo si el espacio vacio no esta en la fila 0.

                matriz[coord_vacio[0]][vacio_colu],matriz[coord_vacio[0] - 1][vacio_colu] = matriz[coord_vacio[0] - 1][vacio_colu],matriz[coord_vacio[0]][vacio_colu]
                coord_vacio[0] = coord_vacio[0] - 1

        if movimiento == MOV_ARRIBA: #Ejecuta lo de abajo si y solo si el espacio vacio no esta en la ultima fila.
            if coord_vacio[0] != NUMERO_FILA - 1: 

                matriz[coord_vacio[0]][vacio_colu],matriz[coord_vacio[0] + 1][vacio_colu] = matriz[coord_vacio[0] + 1][vacio_colu],matriz[coord_vacio[0]][vacio_colu]
                coord_vacio[0] = coord_vacio[0] + 1

        if movimiento == MOV_DERECHA:#Ejecuta lo de abajo si y solo si el espacio vacio no esta en la primera columna
            if vacio_colu != 0:

                matriz[coord_vacio[0]][vacio_colu],matriz[coord_vacio[0]][vacio_colu - 1] = matriz[coord_vacio[0]][vacio_colu - 1],matriz[coord_vacio[0]][vacio_colu]
                vacio_colu = vacio_colu - 1

        if movimiento == MOV_IZQUIERDA :#Ejecuta lo de abajo si y solo si el espacio vacio no esta en la ultima columna
            if vacio_colu != NUMERO_COLU - 1:

                matriz[coord_vacio[0]][vacio_colu],matriz[coord_vacio[0]][vacio_colu + 1] = matriz[coord_vacio[0]][vacio_colu + 1],matriz[coord_vacio[0]][vacio_colu]
                # a,b = b,a
                vacio_colu = vacio_colu + 1
       

   #print()
   #print(coord_vacio)
   #print()

    for i in range(len(matriz)):
        print(matriz[i])     

# Funciones debug BORRAR DESPUES
#mover_vacio(["Arriba","Arriba","Arriba","Arriba","Arriba","Arriba","Arriba","Arriba","Arriba","Arriba","Abajo",])
#print(generar_cantidad_cuadrados())

# Funcion para que queda linda la matriz, anadir ljust y rjust
#for i in range(len(matriz)):
#        print(matriz[i])
    
# input 
