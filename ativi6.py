def teste_maior(maior):
	
	juju = maior[0]
	
	for aux in maior:
		if aux > juju :
			
			juju = aux
			
	return juju


def teste_menor(menor):
	
	cortes = menor[0]
	
	for aux in menor:
		if aux < cortes:
			
			cortes = aux
			
	return cortes

def principal():
	
	dog = 0
	bolo = []
	bolinho = []
	while dog < 7:
		
		menor,maior = map(int,input().split())
		bolinho.append(menor)
		bolo.append(maior)
		
		dog += 1
		
	print("Temperatura Minima da Semana: ",teste_menor(bolinho),"C")
	print("Temperatura Maxima da Semana: ",teste_maior(bolo),"C")


principal()
