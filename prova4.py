alfa = {}
beta = {}
gama = {}
delta = {}
epsilon = {}
zeta = {}
eta = {}
teta = {}


num_registros = int(input())

for i in range(num_registros):
    area, especie, quantidade = input().split()
    quantidade = int(quantidade)
    if area == "Alfa":
        alfa[especie] = quantidade
    elif area == "Beta":
        beta[especie] = quantidade
    elif area == "Gama":
        gama[especie] = quantidade
    elif area == "Delta":
        delta[especie] = quantidade
    elif area == "Epsilon":
        epsilon[especie] = quantidade
    elif area == "Zeta":
        zeta[especie] = quantidade
    elif area == "Eta":
        eta[especie] = quantidade
	elif area == "Teta":
		teta[especie] = quantidade

total_geral = 0
for dicionario in [alfa, beta, gama, delta, epsilon, zeta, eta, teta]:
	total_area = 0
	for quantidade in dicionario.values():
		total_area += quantidade
		total_geral += quantidade

print("Alfa")
print("Zorgons",alfa['Zorgons'])
print("Xentarians",alfa['Xentarians'])
print("Velerianos")
print("Krallians")
print("Neptarions")

print("Beta")
print("Zorgons")
print("Xentarians")
print("Velerianos")
print("Krallians",beta['Krallians'])
print("Neptarions",beta['Neptarions'])

print("Gama")
print("Zorgons")
print("Xentarians")
print("Velerianos")
print("Krallians")
print("Neptarions")

print("Delta")
print("Zorgons")
print("Xentarians")
print("Velerianos")
print("Krallians")
print("Neptarions")

print("Epsilon")
print("Zorgons")
print("Xentarians")
print("Velerianos")
print("Krallians")
print("Neptarions")

print("Zeta")
print("Zorgons")
print("Xentarians")
print("Velerianos")
print("Krallians")
print("Neptarions")

print("Eta")
print("Zorgons")
print("Xentarians")
print("Velerianos")
print("Krallians")
print("Neptarions")

print("Teta")
print("Zorgons")
print("Xentarians")
print("Velerianos")
print("Krallians")
print("Neptarions")

print("Total geral: " + str(total_geral))

"""
4
Alfa Zorgons 20
Alfa Xentarians 10
Beta Krallians 5
Beta Neptarions 2
"""

