quantidade_candidatos = 0

nota_candidato = int(input())

suposicao_maior = nota_candidato

while nota_candidato >= 0:

	quantidade_candidatos += 1

	print("Comparação", nota_candidato, suposicao_maior)

	if nota_candidato > suposicao_maior:
		suposicao_maior = nota_candidato
		
	nota_candidato = int(input())
	

print(quantidade_candidatos)
print(suposicao_maior)
