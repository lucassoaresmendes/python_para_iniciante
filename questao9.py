consumo = int(input())

if consumo <= 10:
	preco = 5
elif 10 < consumo <= 100:
	preco = (consumo*0.6)+2
elif consumo > 100:
	preco = (100*0.6)+3
	if consumo <= 150:
		preco = preco+((consumo-100)*0.85)
	elif consumo > 150:
		preco = preco+(50*0.85)
		preco = preco+((consumo - 150)*1.20)

print(preco)
