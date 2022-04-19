def calcularProdVectorial(x1, y1, z1, x2, y2, z2):
    """Recibe las coordenadas de dos vectores en R3 y devuelve el producto vectorial

    (x1 y1 z1)
  × (x2 y2 z2)
    ----------
(y1*z2-y2*z1),-(x1*z2-x2*z1),(x1*y2-x2*y1)"""

    vectOrtogonal_x, vectOrtogonal_y, vectOrtogonal_z = (y1*z2 - y2*z1), -(x1*z2 - x2*z1), (x1*y2 - x2*y1)

    return vectOrtogonal_x, vectOrtogonal_y, vectOrtogonal_z

assert calcularProdVectorial(54, 12, 29, 1, 11, 12) == (-175, -619, 582)
assert calcularProdVectorial(71, 52, 24, 1, 11, 6) == (48, -402, 729)
assert calcularProdVectorial(726, 434, 110, 488, 962, 820) == (250060, -541640, 486620)
assert calcularProdVectorial(62, 12, 198, 380, 334, 490) == (-60252, 44860, 16148)
assert calcularProdVectorial(-85, 807, 964, 462, 101, 474) == (285154, 485658, -381419)
assert calcularProdVectorial(746, 466, 396, 910, 138, 289) == (80026, 144766, -321112)
assert calcularProdVectorial(-15, 53, 105, 413, 149, 270) == (-1335, 47415, -24124)
assert calcularProdVectorial(291, 413, 227, 166, 638, 284) == (-27534, -44962, 117100)
assert calcularProdVectorial(192, 362, 397, 249, 598, 50) == (-219306, 89253, 24678)
assert calcularProdVectorial(781, 520, 996, 348, 68, 215) == (44072, 178693, -127852)
assert calcularProdVectorial(459, 971, 201, 582, 569, 703) == (568244, -205695, -303951)
assert calcularProdVectorial(754, 968, 956, 231, 901, -31) == (-891364, 244210, 455746)
