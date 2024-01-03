def primo_x(x):
	cont_x = 0
	for n in range(2,x+1):
		primo = True
		i = 2
		while i < n and primo:
			if n % i == 0:
				primo = False
			i += 1
		if primo:
			cont_x += n
	return cont_x

def primo_y(y):
	cont_y = 0
	for n in range(2,y+1):
		primo = True
		i = 2
		while i < n and primo:
			if n % i == 0:
				primo = False
			i += 1
		if primo:
			cont_y += n
	return cont_y

def somatorio(x,y):
	expressao = (primo_x(x) * primo_y(y))/(primo_x(x) + primo_y(y))
	return expressao

def principal():
	x , y = map(int, input().split())
	print(somatorio(x,y))
principal()

