
numeros_reais=list(map(float, input().split()))


num1,num2=map(int,input().split())


somatorio=0
posicao=0

for posicao in range(num1,num2+1):
	
	somatorio+=numeros_reais[posicao]

	
print (somatorio)

