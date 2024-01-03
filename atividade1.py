def fat_n(n):

	
	
	acumula_n = 2
	for num in range(2,n+1):
		acumula_n *= num

		
	return acumula_n

def fat_p(p):


	acumula_p = 2
	for num in range(2,p+1):
		acumula_p *= num

		
	return acumula_p

def fat_n_p(n,p):



	acumula_n_p = 2
	m = n-p
	for num in range(2,m+1):
		acumula_n_p *= num

		
	return acumula_n_p
	
def principal():

	
	n, p= map(int,input().split())
	combinacao = (fat_n(n))/(fat_p(p)*fat_n_p(n,p))*2

	
	print(combinacao)

principal()
