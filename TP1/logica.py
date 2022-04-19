MATRIZ_COLUMNAS = 7
MATRIZ_FILAS    = 5

def generar_cantidad_cuadrados():
    '''
    Funcion que genera una lista de numeros, dependiendo de la cantidad de filas y columnas
    La formula para hallar esto es (MATRIZ_FILAS x MATRIZ_COLUMNAS) - 1
    '''
    cantidad_de_cuadrados = MATRIZ_COLUMNAS * MATRIZ_FILAS
    lista_con_cuadrados = []

    for i in range(1,cantidad_de_cuadrados):
        lista_con_cuadrados.append(i)
    lista_con_cuadrados.append("")

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
    for fila in range(MATRIZ_FILAS):
        matriz.append([])
        for columna in range(MATRIZ_COLUMNAS):
            matriz[fila].append(columna)
    return matriz

# Funciones debug BORRAR DESPUES
#print(generar_matriz())
print(generar_cantidad_cuadrados())
