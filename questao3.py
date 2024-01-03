numero = int(input())

contador = 0
contador_negativo = 0



while contador <= 13:
	
	if numero < 0:
		contador_negativo += 1
		
	contador += 1
	numero = int(input())

print(contador_negativo)


	
