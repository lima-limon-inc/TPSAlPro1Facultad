import os
# Archivo encargado de procesar archivos

def leer_movimientos(archivo):
    '''
    Funcion que se encarga de leer el archivos que contiene los movimientos de las distintas piezas.
    Recibe:
        0. archivos -> str. Direccion del archivo que queremos leer
    Devuele:
        0. diccionario_movimientos -> dict. Diccionario con todos los movimientos validos de cada pieza
    '''
    diccionario_movimientos = {}
    with open(archivo, "r") as f:
        for linea in f:
            pieza, dir_x_dir_y, extensible = linea.rstrip("\n").split(",")
            extensible =  extensible.capitalize()
            diccionario_movimientos[pieza] = diccionario_movimientos.get(pieza, set()) #"Sobreescribe" el valor si ya existe consigo mismo, caso contrario crea una lista vacia como valor

            dir_x, dir_y = dir_x_dir_y.split(";")
            dir_x, dir_y = int(dir_x), int(dir_y)

            repeticiones = 8 if extensible == "True" else 2 #En realidad son 7 repeticiones, pero pongo 8 dedbido a que range no incluye el ultimo elemento (mismo con el 2)

            for i in range(1, repeticiones):
                diccionario_movimientos[pieza].add((dir_x * i, dir_y * i))

    return diccionario_movimientos

def guardar_tablero(archivo, tablero, pieza_seleccionada):
    '''
    Funcion que se encarga de guardar un tablero cualquiera (incluyendo la pieza_seleccionada)
    Recibe:
        0. tablero -> dict. Diccionario que representa el tablero de juego
        1. pieza_seleccionada -> tuple. Coordenada de la pieza que el con la que usuario empieza
    Devuele:
        0. None
        Funcion impropia, solo tiene efectos secundarios
    '''
    with open(archivo, "w") as f:
        f.write(str(pieza_seleccionada)[1:-1] + "\n" )
        for coordenada, pieza in tablero.items():
            f.write(str(coordenada)[1:-1] + ":" +  str(pieza) + "\n" )

def leer_archivo(archivo): #TODO: Anadir procesamiento de lo que pasa si el archivo no existe
    '''
    Funcion que se encarga de leer un archivo y devolver los valores procesados
    Recibe:
        0. archivos -> str. Direccion del archivo que queremos leer
    Devuelve:
        0. tablero -> dict. Diccionario que representa el tablero de juego
        1. pieza_seleccionada -> tuple. Coordenada de la pieza que el con la que usuario empieza
    '''
    with open(archivo, "r") as f:
        pieza_seleccionada =  tuple([int(i) for i in f.readline().rstrip().split(", ")])
        tablero = {}
        for linea in f:
            casilla, pieza = linea.rstrip().split(":")
            casilla = tuple([int(i) for i in casilla.split(", ")])
            tablero[casilla] = pieza
            tablero[casilla] = (casilla[0], casilla[1], pieza)

        return tablero, pieza_seleccionada


