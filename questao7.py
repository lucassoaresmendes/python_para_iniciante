retorno = float(input())
numero_meses = int(input())
contador = 0
somatorio = 0

while contador < numero_meses:
	
	valores = float(input())
	contador += 1
	
	somatorio = somatorio+valores
	somatorio = somatorio + ((retorno/100)*somatorio)

print(somatorio)
