#entrada de dados
n, i, j = map(int,input().split())

#Reoetição: gerar números a partir de 0
numero = 0
contadora_multiplos = 0

while contadora_multiplos < n:
	
#Condicional: analisar divisibilidade i j
	if numero % i == 0 or numero % j == 0:
		contadora_multiplos += 1
		print(numero)
	
	numero += 1
