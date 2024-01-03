def fatorial(a):
	contadora = a
	acumuladora = 1
	while contadora >= 1:
		acumuladora = acumuladora * contadora
		contadora -= 1
	return acumuladora

def fibonacci(a):
	
	fib = 0
	fib_1 = 0
	fib_2 = 0
	
	i = 1
	while i <= a:
		if i == 1:
			fib = 1
		elif i == 2:
			fib = 1
			fib_2 = 1
			fib_1 = 1
		else:
			fib = fib_1 + fib_2
			fib_2 = fib_1
			fib_1 = fib
		i += 1
	return fib

def controleOperacao(a,b):#a é uma string, b é um número inteiro
	if a == "fatorial":
		return fatorial(b)
	elif a == "fibonacci":
		return fibonacci(b)
	

def principal():
	x = int(input())
	op = input()
	print(controleOperacao(op,x))

principal()
