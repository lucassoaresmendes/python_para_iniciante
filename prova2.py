'''
comparar triangulo
3 lados iguais = equilatero
2 lados iguais = isoceles
3 lados diferentes = escaleno
'''

x, y, z =  map(float, input().split())

if (x + y < z) or (x + z < y) or (y + z < x):
	print('Nao é um triangulo')
elif (x == y) and (x == z) :
	print('Equilatero')
elif (x==y) or (x==z) or (y==z):
	print('Isósceles')
else:
	print('Escaleno')
