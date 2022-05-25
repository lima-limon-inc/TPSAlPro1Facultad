# Archivo encargado de procesar archivos

def leer_movimientos(archivo):
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