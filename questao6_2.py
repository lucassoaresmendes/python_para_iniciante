t=0
i=0
soma=0
media=0
temperatura=[]

while len(temperatura)<7 and t>=0:
	t=int(input())
	if t>=0:
		temperatura.append(t)
		
		
for i in range (len(temperatura)):
	soma=soma+temperatura[i]
	
media= soma/len(temperatura)
if media >=0 and media <=3:
	print(round(media,2),"C")
	print("Alerta de Temperaturas Extremas – Tendência de forte frio nos próximos dias")
	for elemento in temperatura:
		if elemento > media:
			print(elemento)
else:
	print(round(media,2),"C")
	for elemento in temperatura:
		if elemento > media:
			print(elemento)
