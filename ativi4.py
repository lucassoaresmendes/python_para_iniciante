def confere_sequencia(x,y,vetor_um,vetor_dois):
	
	um = 0
	bolo = []
	
	while um < x:
		
		dois = 0
		i = 10
		j = 1
		
		while dois < y and um < x:
			
			dog = []
			
			if vetor_um[um] == vetor_dois[dois]:
				dog.append(vetor_dois[dois])
				
				numeroAnterior_um = vetor_um[um]
				numeroAnterior_dois = vetor_dois[dois]
				
				um += 1
				dois += 1
				
				if um < x and dois < y:
					
					while vetor_um[um] == vetor_dois[dois] and numeroAnterior_um + 1 == vetor_um[um] and numeroAnterior_dois + 1 == vetor_dois[dois] and i == 10 and dois < y and um < x:
						dog.append(vetor_dois[dois])
						
						numeroAnterior_um = vetor_um[um]
						numeroAnterior_dois = vetor_dois[dois]
						
						um += 1
						dois += 1
						
						j = 0
						
						if um == x or dois == y:
							
							i = 20
							um -= 1
							dois -= 1
							
					if i == 20:
						
						um += 1
						dois += 1
						
				else:
					
					um -= 1
				armazena = len(dog)
				
				if armazena > 1:
					bolo.append(dog)
					
			else:
				dois += 1
				
		if j == 1:
			um += 1
			
	return bolo
	
def principal():
	
	x = int(input())
	y = int(input())
	
	vetor_um = list(map(int,input().split()))
	vetor_dois = list(map(int,input().split()))
	
	juliana = confere_sequencia(x,y,vetor_um,vetor_dois)
	
	bolinho = len(juliana)
	
	if bolinho > 0:
		
		for aux in juliana:
			for elemento in range(len(aux)):
				
				print(aux[elemento],end=" ")
			print("")
			
	else:
		print("ERRO")


principal()

