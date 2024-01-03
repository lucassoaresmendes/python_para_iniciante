'''
def media5valores(A,B,C,D,E):#"A,B,C,D,E são parametros formais"
	soma = A+B+C+D+E
	media = soma/5
	return soma, media

#Energia
resposta1, resposta2 = media5valores(100,200,300,100,400)#Para exibir sem parentese e sem virgula

print(resposta1,resposta2)#valores dentro do parenteses são chamado de parâmetros reais

#Água
print(media5valores(80,100,120,150,110))

#Materiais de limpeza
print(media5valores(50,100,70,100,80))
'''
def media5valores(A,B,C,D,E):#"A,B,C,D,E são parametros formais"
	soma = A+B+C+D+E
	media = soma/5
	return soma, media
X = int(input())
Y = int(input())
O = int(input())
P = int(input())
Q = int(input())
soma,media = media5valores(X,Y,O,P,Q)
print(soma,media)
