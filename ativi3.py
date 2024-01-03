LinhaColuna = int(input())
princ = 0
secun = 0
matriz =[]

for i in range(LinhaColuna):
	dog=list(map(float,input().split()))
	matriz.append(dog)

y = matriz[0][len(matriz)-1]

for elemento in range(len(matriz)):
	
	 secun += matriz[elemento][len(matriz)-1-elemento]
	 
	 if (matriz[elemento][len(matriz)-1-elemento]) < y:
		 y = matriz[elemento][len(matriz)-1-elemento]
	
x = matriz[0][0]

for elemento in range(LinhaColuna):
	
	princ += matriz[elemento][elemento]
	
	if (matriz[elemento][elemento]) > x:
		x = matriz[elemento][elemento]
		
		 
print(x)
print(princ)
print(y)
print(secun)

