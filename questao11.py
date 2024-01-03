from math import *

valor_salario = float(input())
contribuicao = 0

if valor_salario >= 0 and valor_salario <= 1693.72:
	contribuicao = valor_salario*(0.08)
elif valor_salario > 1693.72 and valor_salario <= 2822.90:
	contribuicao = valor_salario*(0.09)
elif valor_salario > 2822.90 and valor_salario <= 5645.80:
	contribuicao = valor_salario * (0.11)
elif valor_salario > 5645.80:
	contribuicao = 5645.80 * 0.11

print (contribuicao)

