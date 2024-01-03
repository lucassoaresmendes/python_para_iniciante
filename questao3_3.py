def main():
# vamos declarar e construir uma matriz de três linhas
# e três colunas
	linhas, colunas = (3, 3)
	matriz = [[0 for x in range(linhas)] for y in range(colunas)]
	soma_diagonal = 0 # guarda a soma dos elementos na diagonal
# principal
 
# vamos ler os elementos da matriz
	for i in range(len(matriz)):
		for j in range(len(matriz[i])):
			matriz[i][j] = int(input("Informe o valor para a linha " + str(i) + " e coluna " + str(j) + ": "))
	print()

	for i in range(len(matriz)):
		for j in range(len(matriz[i])):
			print(matriz[i][j], end='  ')
		print()
 
# vamos calcular a soma dos elementos da diagonal   
# principal
	for i in range(len(matriz)):
		for j in range(len(matriz[i])):
			if i == j:
				soma_diagonal = soma_diagonal + matriz[i][j]
 
# finalmente mostramos a soma da diagonal principal
	print("\nA soma dos elementos da diagonal principal é: %d" %soma_diagonal)  
 
if __name__== "__main__":
	main()

