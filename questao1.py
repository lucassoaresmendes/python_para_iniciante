n = int(input())
numero = []
contadora = 0
somatorio = 0

while contadora < n:
	escalar = int(input())
	somatorio += escalar
	numero.append(escalar)
	contadora += 1
print (somatorio)
