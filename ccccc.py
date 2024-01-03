fita_dna = input()

l = list(fita_dna)

for elemento in fita_dna:
	if l[elemento] == "T":
		l[elemento] = "U"

	fita_dna = "".join(l)
print(fita_dna)
'''
for elemento in fita_dna:
	if elemento == "T":
		fita_dna[elemento] = "U"

print(fita_dna)


GATGGAACTTGACTACGTAAATT
fita_dna = input()

for elemento in fita_dna:
	if elemento == "T":
		fita_dna[elemento] = "U"
		
print(fita_dna)

'''

