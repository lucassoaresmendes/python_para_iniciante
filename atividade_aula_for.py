lista_par = []
lista_impar = []

for i in range(10):
	escalar = int(input())
	if escalar % 2 == 0:
		lista_par.append(escalar)
	else:
		lista_impar.append(escalar)

print(lista_par)
print(lista_impar)		
