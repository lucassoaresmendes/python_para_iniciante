numero = []
contadora = 0


while contadora < 10:
	entrada = int(input()) 
	numero.append(entrada)
	contadora += 1

pares = []
impares = []

posicao = 0

while posicao < 10:
	if numero[posicao] % 2 == 0:
		pares.append(numero[posicao])
	else:
		impares.append(numero[posicao])
	posicao += 1

print(numero)
print(pares)
print(impares)
