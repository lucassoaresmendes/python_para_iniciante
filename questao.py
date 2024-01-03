#Questao 1
"""
import math

def vc(d,r):
	velocidade=((math.pi)*d*r)/1000
	return velocidade

def principal():
	d=float(input())
	r=int(input())
	print(round(vc(d,r),2),"m/min")
principal()

"""

#Questao 2
"""
t=0
i=0
soma=0
media=0
temp=[]

while len(temp)<7 and t>=0:
	t=int(input())
	if t>=0:
		temp.append(t)

for i in range(len(temp)):
	soma+=temp[i]
	
media = soma/len(temp)
if media>=0 and media<=3:
	print(round(media,2),"C")
	print("Alerta de Temperaturas Extremas – Tendência de forte frio nos próximos dias")
	for elem in temp:
		if elem > media:
			print(elem)

else:
	print(round(media,2),"C")
	for elem in temp:
		if elem > media:
			print(elem)

"""

#Questão 3
"""
linha_coluna = int(input())
matriz = []
soma_princ = 0
soma_secun = 0

for i in range(linha_coluna):
	lista = list(map(float,input().split()))
	matriz.append(lista)
prim = matriz[0][0]

for j in range (linha_coluna):
	soma_princ += matriz[j][j]
	if (matriz[j][j]) > prim:
		prim = matriz [j][j]
sec = matriz[0][len(matriz)-1]
for elem in range (len(matriz)):
	 soma_secun += matriz[elem][len(matriz)-1-elem]
	 if (matriz[elem][len(matriz)-1-elem]) < sec:
		 sec = matriz[elem][len(matriz)-1-elem]

print(prim)
print(soma_princ)
print(sec)
print(soma_secun)
"""

		
#Questão 4
"""def r_s(tam1,tam2,lista1,lista2):

	
	pos1=0
	seq=[]
	
	while pos1<tam1:

		
		pos2=0
		m=10
		n=1
		
		while pos2<tam2 and pos1<tam1:

			
			atual=[]
			
			if lista1[pos1] == lista2[pos2]:

				
				atual.append(lista2[pos2])
				
				anterior1 = lista1 [pos1]
				
				anterior2 = lista2 [pos2]
				
				pos1 += 1
				
				pos2 += 1
				
				if pos1 < tam1 and pos2 < tam2:
					
					while lista1 [pos1] == lista2 [pos2] and anterior1 + 1 == lista1 [pos1] and anterior2 + 1== lista2[pos2] and m == 10 and pos2 < tam2 and pos1 < tam1:
						
						atual.append(lista2[pos2])
						
						anterior1 = lista1[pos1]
						
						anterior2 = lista2[pos2]
						
						pos1 += 1
						
						pos2 += 1
						
						n = 0
						
						if pos1 == tam1 or pos2 == tam2:
							
							m = 20
							pos1 -= 1
							pos2 -= 1
							
					if m == 20:
						
						pos1 += 1
						pos2 += 1
						
				else:
					
					pos1 -= 1
					
				x = len(atual)
				
				if x > 1:
					
					seq.append(atual)
			else:
				
				pos2 += 1
		
		if n == 1:
			
			pos1 += 1
			
	return seq
	

def principal():
	
	tam1 = int(input())
	tam2 = int(input())
	
	lista1 = list(map(int,input().split()))
	lista2 = list(map(int,input().split()))
	
	seq = r_s(tam1,tam2,lista1,lista2)
	
	x = len(seq)
	
	if x > 0:
		
		for b in seq:
			for c in range(len(b)):
				print(b[c], end=" ")
			print("")
			
	else:
		
		print("ERRO")
principal()
"""

#Questão 5

"""
l_c=int(input())
matriz=[]
cont=0
cont_eve=0

for i in range(l_c):
	l=list(map(int,input().split()))
	matriz.append(l)
even=int(input())

while cont < even:
	x,y=map(int,input().split())
	if matriz[x][y]==1:
		cont_eve+=1
	cont+=1
print(cont_eve)
"""

#Questão 6

"""
def principal():
	contador = 0
	l_max = []
	l_min = []
	while contador < 7:
		x,y = map(int,input().split())
		l_min.append(x)
		l_max.append(y)
		contador = contador + 1
	print("Temperatura Minima da Semana: ",Temperatura_Minima(l_min),"C")
	print("Temperatura Maxima da Semana: ",Temperatura_Maxima(l_max),"C")
def Temperatura_Minima(x):
	men = x[0]
	for i in x:
		if i < men:
			men = i
	return men
def Temperatura_Maxima(y):
	mai = y[0]
	for i in y:
		if i > mai :
			mai = i
	return mai
principal()
"""
