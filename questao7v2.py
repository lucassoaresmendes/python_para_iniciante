milisegundos=int(input())

horas = milisegundos//3600000
minutos = (milisegundos-(horas*3600000))//60000
segundos=(milisegundos-(horas*3600000)-(minutos*60000))/1000
print(int(horas),":",int(minutos),":",float(segundos))	
