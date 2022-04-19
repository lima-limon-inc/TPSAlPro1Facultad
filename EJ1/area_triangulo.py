""" Consigna:
d) Utilizando las funciones anteriores, escribir una función que reciba las coordenadas de 3 puntos en R3 y devuelva el área del triángulo que conforman.
Ayuda: Si A, B y C son 3 puntos en el espacio, la norma del producto vectorial ⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗ AB × ⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗ AC es igual al doble del área del triángulo ABC."""

from vectores import calcularProdVectorial, norma, diferencia

def calcularAreaTriangulo(Ax, Ay, Az, Bx, By, Bz, Cx, Cy, Cz):
    """Funcion que calcula el area de un triangulo dados tres puntos"""
    DifABx, DifABy, DifABz = diferencia(Ax, Ay, Az, Bx, By, Bz) 
    DifACx, DifACy, DifACz = diferencia(Ax, Ay, Az, Cx, Cy, Cz) 
    
    ProdVectABACx, ProdVectABACy, ProdVectABACz = calcularProdVectorial(DifABx, DifABy, DifABz, DifACx, DifACy, DifACz)
    
    Norma = norma(ProdVectABACx, ProdVectABACy, ProdVectABACz)

    areaTriangulo = Norma/2

    return areaTriangulo

def main():
    print("Area triangulo 1:" , str(calcularAreaTriangulo(1,2,6,9,5,8,3,8,9)))
    print("Area triangulo 2:" , str(calcularAreaTriangulo(7,4,8,3,2,5,2,5,2)))
    print("Area triangulo 3:" , str(calcularAreaTriangulo(4,8,2,1,1,7,3,5,1)))

main()
