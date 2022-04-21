matriz = []

elemento = 1

for fila in range(4):
    matriz.append([])
    for column in range(4):
        matriz[fila].append(elemento)
        elemento += 1
matriz[-1][-1] = "E"
print(matriz)
