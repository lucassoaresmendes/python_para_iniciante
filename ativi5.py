ju = []

dog = 0
bolo = 0
bolinho = 0

indica = int(input())

while dog < indica:
	
	armazena = list(map(int,input().split()))
	ju.append(armazena)
	
	dog += 1
	
explosao = int(input())

while bolo < explosao:
	
	i,j = map(int,input().split())
	
	if ju[i][j] == 1:
		bolinho += 1
		
	bolo += 1
	
print(bolinho)
