num = int(input())
conta = 0

for n in range(2,num+1):
	print(n , end = " -> ")

	primo = True

	i = 2

	while i < n and primo:
		if n % i == 0:
			primo = False
		i += 1

	if primo:
		conta += n
		print("SIM")
	else:
		print("NÃO")

print(conta)
