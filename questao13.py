l = float(input())
n = int(input())
comprimento_onda = 2*l/n
i = 1
linha1 = "   _ "
linha2 = "  | |"
linha3 = "|_|  "
while i <= n and i != 0:
    if n % 2 == 0:
        print(linha1*(n//2))
        print(linha2*(n//2))
        print(linha3*(n//2))
        i -= 1
    else:
        print(linha1*(n//2))
        print(linha2*(n//2))
        print(linha3*(n//2+1))
        i -= 1
print("Comprimento de onda =",round(comprimento_onda,2))
