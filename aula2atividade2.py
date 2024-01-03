"""
	.slit() é utilizado quando se tem duas variaveis na mesma linha, onde
	ele separa os dados separados pelo espaço

	map() é utilizado para converter as strings em seus tipos apropriados

	 
"""
from math import *

nivel = int(input())

if nivel >= 0 and nivel<= 3:
	print("nivel de gravidade baixo")

elif nivel >3 and nivel<= 6:
	print("Nível de gravidade médio")
elif nivel > 6 and nivel<= 10:
	print("Nível de gravidade alto")
else:
	print("ERROOOOOOO")
	
