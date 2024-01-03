def media5valores(A,B,C,D,E):#"A,B,C,D,E são parametros formais"
	soma = A+B+C+D+E
	media = soma/5
	return media

#Subprograma de controle geral
def principal():
	contador = 0
	while contador < 3:
		X = int(input())
		Y = int(input())
		O = int(input())
		P = int(input())
		Q = int(input())
		media = media5valores(X,Y,O,P,Q)
		print("Média dos gastos",media)
		contador+=1

principal()	
