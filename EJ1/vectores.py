# Programa que a va a tener todas las funciones necesarias para calcular el area de un triangulo
def calcularProdVectorial(x1, y1, z1, x2, y2, z2):
    """Recibe las coordenadas de dos vectores en R3 y devuelve el producto vectorial

    (x1 y1 z1)
  × (x2 y2 z2)
    ----------
(y1*z2-y2*z1),-(x1*z2-x2*z1),(x1*y2-x2*y1)"""

    vectOrtogonal_x, vectOrtogonal_y, vectOrtogonal_z = (y1*z2 - y2*z1), -(x1*z2 - x2*z1), (x1*y2 - x2*y1)

    return vectOrtogonal_x, vectOrtogonal_y, vectOrtogonal_z

def norma(x, y, z):
    """Recibe un vector en R3 y devuelve su norma"""
    return (x**2 + y**2 + z**2) ** 0.5

def diferencia(x1, y1, z1, x2, y2, z2):
    """Recibe las coordenadas de dos vectores en R3 y devuelve su diferencia"""
    dif_x = x1 - x2
    dif_y = y1 - y2
    dif_z = z1 - z2
    return dif_x, dif_y, dif_z

