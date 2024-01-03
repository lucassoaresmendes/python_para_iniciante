temperatura = list(map(float,input().split()))
soma = 0

for elemento in temperatura:
	soma = soma + elemento

media = soma / len(temperatura)

for posicao in range(len(temperatura)):
	if temperatura[posicao] > media:
		print(temperatura[posicao],posicao+1)

"""
for posicao in range(len(temperatura)):
	soma = soma + temperatura[posicao]

"""
