dog = 0
bolo = 0
bolinho = 0

media_temp = 0
lista_temp = []

while bolo < 7 and dog >= 0:
	
	dog = int(input())
	if dog >= 0:
		lista_temp.append(dog)
	bolo += 1

for aux in range(len(lista_temp)):
	
	bolinho += lista_temp[aux]
	
media_temp = bolinho / len(lista_temp)

if media_temp >= 0 and media_temp <= 3:
	
	print(round(media_temp,2),"C")
	print("Alerta de Temperaturas Extremas – Tendência de forte frio nos próximos dias")
	
	for elemento in lista_temp:
		if elemento > media_temp:
			print(elemento)
			
else:
	
	print(round(media_temp,2),"C")
	
	for elemento in lista_temp:
		if elemento > media_temp:
			print(elemento)

