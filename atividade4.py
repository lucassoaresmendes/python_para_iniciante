dna = input()

cont_a = 0
cont_c = 0
cont_g = 0
cont_t = 0
for elemento in dna:
	if elemento == "A":
		cont_a += (71.03711 + 18.01056)
	elif elemento == "C":
		cont_c += (103.00919 + 18.01056)
	elif elemento == "G":
		cont_g += (57.02146 + 18.01056)
	elif elemento == "T":
		cont_t += (101.04768 + 18.01056)
		
print(cont_a + cont_c + cont_g + cont_t)

