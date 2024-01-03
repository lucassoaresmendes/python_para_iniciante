numeros = int(input())

contador = 0
somatorio = 0
positivo = 0
negativo = 0
media = 0

while numeros > 0 or numeros < 0:
	if numeros > 0:
		positivo += 1
		
	if numeros < 0:
		negativo += 1

	somatorio += numeros
	contador += 1
	numeros = int(input())	

media = somatorio / contador
percentual_posi = positivo/contador
percentual_nega = negativo/contador

print(media)
print(positivo)
print(negativo)
print(percentual_posi)
print(percentual_nega)
	
