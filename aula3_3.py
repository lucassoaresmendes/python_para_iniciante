"""
Contadores: usadas para contar o número de repetições de um laço
que satisfaz as necessidades de um dado problema qualquer.

"""

numero = int(input())
contador = 0

while numero >= 0:
		
	if numero % 2 == 0:
		contador +=1

	numero = int(input())
		
print(contador)
