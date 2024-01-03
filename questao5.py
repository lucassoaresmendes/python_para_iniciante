"""contadora_tent= 0
senha = ""
while contadora_tent < 3 and senha != "001001000111":
    senha = input()
    contadora_tent += 1
if senha == "001001000111":
    print("acessou arma", contadora_tent)
else:
    print("disparou alarme", contadora_tent)
"""
contadora_tent= 0
senha = input()
codigo = "001001000111"
while contadora_tent < 3:
	contadora_tent += 1
	if senha == codigo:
		print("acessou arma", contadora_tent)
		break
	elif contadora_tent == 3:
		print("disparou alarme", contadora_tent)
		break
	senha = input()

