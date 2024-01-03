"""
Leitura de um número inteiro

Descobrir quantas notas de 50

Descobrir quantas notas de 10

Descobrir quantas notas de 5

Descobrir quantas notas de 1

Exibir as quantidades
"""
valorSaque = int(input("Digite o valor no qual deseja sacar:"))

quantidadeNotas50 = valorSaque // 50
restoSaque = valorSaque % 50

quantidadeNotas10 = restoSaque // 10
restoSaque = restoSaque % 10

quantidadeNotas5 = restoSaque // 5
restoSaque = restoSaque % 5

quantidadeNotas1 = restoSaque

print("Sao necessárias",quantidadeNotas50,"notas de 50")
print("Sao necessárias",quantidadeNotas10,"notas de 10")
print("Sao necessárias",quantidadeNotas5,"notas de 5")
print("Sao necessárias",quantidadeNotas1,"notas de 1")


