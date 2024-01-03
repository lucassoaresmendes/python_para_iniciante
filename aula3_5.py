"""
Sentinelas: variáveis utilizadas para controlar uma estrutura de
repetição (seu valor lógico é verificado para continuar ou interromper a
estrutura)

"""

sentinela = True
contador = 0
somatorio = 0

while sentinela == True:
	numero = int(input())
	if numero > 0:
		contador +=1
		somatorio += numero

		if somatorio >= 200:
			sentinela = False
		if contador >= 20:
			sentinela = False

	else:
		sentinela = False

print(somatorio)
