#Entrada de dados
l, c = map(int,input().split())
m1 = []

for contadora in range(l):
	linha = list(map(float,input().split()))
	m1.append(linha)

m2 = []

for contadora in range(l):
	linha = list(map(float,input().split()))
	m2.append(linha)

#Processamento - soma

for pos_linha in range(l):
	for pos_elemento in range(c):
		print(m1[pos_linha][pos_elemento]+m2[pos_linha][pos_elemento], end = " ")
	print()
