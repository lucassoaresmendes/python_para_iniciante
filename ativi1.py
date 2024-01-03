import math

def Vcorte(dog,rig):
	
	velocidade = (math.pi)*dog*rig
	velocidade = velocidade / 1000
	return velocidade
	
def principal():
	
	dog = float(input())
	rig = int(input())
	
	print(round(Vcorte(dog,rig),2),"m/min")
	
principal()


