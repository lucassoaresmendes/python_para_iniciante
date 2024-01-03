def calcula(num_naves,pot_naves,pot_terra):
	danoTotal = 0
	for potencia in pot_naves:
		danoTotal += potencia
	energiaRestante = (pot_terra-danoTotal)
	if energiaRestante < 0:
		energiaRestante = 0
	return energiaRestante	

def principal():
	num_naves = int(input())
	if num_naves == 0:
		print("Não há naves para atacar a Terra.")
	elif num_naves > 0:
		
		pot_naves = list(map(int,input().split()))
		pot_terra = int(input())
		
		energia = calcula(num_naves,pot_naves,pot_terra)
		print("Energia restante no escudo de defesa:",energia)
		
		if energia == 0:
			print("A Terra foi invadida!")

	
principal()	
