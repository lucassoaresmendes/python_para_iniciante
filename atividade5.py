from math import *


f=list(map(float,input().split()))

d=list(map(float,input().split()))

t=0

for i in range(len(f)):
	t = t+(f[i]*d[i])



if t>0:

	
	print("Trabalho motor")
	print(t)

	
if t<0:

	
	print("Trabalho resistente")
	print(abs(t))

	
if t==0:

	
	print("Trabalho nulo")
	print(t)



