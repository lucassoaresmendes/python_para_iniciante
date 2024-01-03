quantidade_numero = int(input())
numero = 0

contador_par = 0

contador_impar = 0

contador = 0

while contador < quantidade_numero:
	numero = float(input())
	contador += 1
	if numero % 2 == 0:
		contador_par += 1
	elif numero % 3 == 0:
		contador_impar += 1
	
	

print("Quantidade de pares:",contador_par)
print("")
print("Quantidade de impares:",contador_impar)


