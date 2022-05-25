# Archivo encargado de procesar archivos

def leer_movimientos(archivo):
    diccionario_movimientos = {}
    with open(archivo, "r") as f:
        for linea in f:
            pieza, dir_x_dir_y, extensible = linea.rstrip("\n").split(",")
            extensible =  extensible.capitalize()
            diccionario_movimientos[pieza] = diccionario_movimientos.get(pieza, {"extensible":extensible, "movimientos":[]}) #"Sobreescribe" el valor si ya existe consigo mismo, caso contrario crea una lista vacia como valor

            diccionario_movimientos[pieza]["movimientos"].append((dir_x_dir_y.split(";")))

    return diccionario_movimientos
