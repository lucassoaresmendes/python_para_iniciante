def somatorio(x):


    resultado = 0

    
    for inicio in range(2, x+1):
		
        for m in range(2,inicio):
			
            if(inicio % m == 0): 
                break
                
        else: 
            resultado += inicio


            
    return resultado


def expres(x,y):
	express = (somatorio(x) * somatorio(y))/(somatorio(x) + somatorio(y))

	return express
	
def principal():
    x,y = map(int, input().split())
    

    print(expres(x,y))


principal()
