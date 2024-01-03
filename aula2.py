"""
igualdade ==
maior que >
menor que <
Maior ou igual >=
menor ou igual <=
Diferença !=

"""
from math import *

lado1 = int(input())
lado2 = int(input())
lado3 = int(input())

if lado1<(lado2+lado3)and lado2<(lado1+lado3)and lado3<(lado1+lado2):
	p = (lado1+lado2+lado3)/2
	area = sqrt(p*(p-lado1)*(p-lado2)*(p-lado3))
	print(area)

else:
	print("Medidas não compatíveis")


