from math import *

catetoOposto = float(input())

angulo = int(input())

anguloRadiano = angulo * 0.0174533

hipotenusa = catetoOposto / sin(anguloRadiano)

print(hipotenusa)

