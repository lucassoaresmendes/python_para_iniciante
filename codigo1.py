def funcaoMaior(A,B):
	if A > B:
		return A
	else:
		return B

def principal():
	entrada = int(input())
	contador = 1
	maior_valor = entrada
	while (contador < 10):
		entrada = int(input())
		contador += 1
		maior_valor = funcaoMaior (maior_valor, entrada)
	print(maior_valor)
principal()
