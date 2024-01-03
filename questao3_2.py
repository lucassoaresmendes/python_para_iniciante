# PEGUEI SEU CÓDIGO PARA FACILITAR VOU DEIXAR ELE MAIS EXTENSO MESMO QUE NÃO ESTEJA OTIMIZADO
# Programa para processar e imprimir uma matriz l x c
# Calcular o somatório dos elementos das diagonais principal e secundária
l = int(input("Insira o número de linhas: "))
c = int(input("Insira o número de colunas: "))
matriz = [] #vou apenas descomplicar colocando abaixo uma lista por linha

somaprincipal = 0 # meio desnecessário fazer o casting afinal, python não é uma linguagem fortemente tipada
somasecundaria = 0

for i in range(0, l):
    matriz.append([]) #adiciona uma lista sempre que percorre o loop, mas do seu jeito é mais rápido
    for j in range(0, c):
        matriz[i].append(int(input(f"Insira o elemento {j+1} da linha {i+1}: ")))
        if i == j: # só soma quando o número da linha é o mesmo número da coluna.
            somaprincipal += matriz[i][j] 

for i in range(-1,(-l-1), -1): # percorre a lista do último item ao primeiro
    for j in range(-1,(-c-1), -1): # o mesmo de cima
        if i == j:
            somasecundaria += matriz[i][j]


print("\nElementos da matriz: ")
for i in range(0, l):
    print(*matriz[i]) #printa a matriz sem mostrar os colchetes nem vírgulas
if l == c:
    print("\nSomatório dos elementos da diagonal principal =", somaprincipal)
    print("Somatório dos elementos da diagonal secundária =", somasecundaria)
else:
    print("A matriz não é quadrada, logo não possui diagonais.")
