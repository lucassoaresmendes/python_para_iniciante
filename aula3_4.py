"""

Acumuladores: armazenam valores acumulativos (ex: somatórios ou
produtórios) nas diversas repetições realizadas.

"""

n = int(input())
contador_ciclos = 0
somatorio = 0 #produtorio = 1

while contador_ciclos < n:
	
	numero = float(input())
	contador_ciclos += 1
	somatorio += numero

	
media = somatorio / n #poderia ser contador_ciclos também
print(somatorio)
print(media)
