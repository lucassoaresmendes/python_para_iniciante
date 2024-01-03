"""
Um terrível assassinato aconteceu na última noite, faça um
programa para ajudar os investigadores a encontrar o culpado.
Seu programa deve ler do dispositivo de entrada padrão o nome
de 3 suspeitos e as respostas para cinco perguntas que um
determinado detetive constatou em sua investigação. As
respostas para as perguntas são apenas as palavras sim ou nao.
Cada dado de entrada será fornecido em uma linha diferente.

O programa deve, ao final, exibir no dispositivo de saída padrão
o nome do culpado pelo assassinato, segundo a regra a seguir:
se o detetive respondeu positivamente (sim) a apenas duas
questões, o culpado é o primeiro suspeito; entre 3 e 4 respostas
positivas, o culpado é o segundo suspeito; se foram 5 respostas
positivas, o culpado é o terceiro suspeito; caso contrário, seu
programa deverá exibir o nome de todos os suspeitos (na ordem
em que foram fornecidos)
"""

from math import *

suspeito1 = input("Digite o nome do primeiro suspeito:")
print()
suspeito2 = input("Digite o nome do segundo suspeito:")
print()
suspeito3 = input("Digite o nome do terceiro suspeito:")

contador = 0

print()

print("Responda SIM ou NÃO")
print()

print("A vítima recebeu uma ligação a exatamente uma semana atrás dizendo 7 dias?")
resposta1 = input()
if resposta1 == "sim":
	contador += 1
	
print()

print("A vítima possui cortes e queimaduras severas causadas por um sabre de luz?")
resposta2 = input()
if resposta2 == "sim":
	contador += 1

print()

print("A causa da morte da vítima foi uma severa crise de risos?")
resposta3 = input()
if resposta3 == "sim":
	contador += 1

print()

print("A vítima faleceu durante uma cerimônia de casamento realizada em um castelo medieval?")
resposta4 = input()
if resposta4 == "sim":
	contador += 1

print()

print("Partes do corpo da vítima foram encontradas dentro de uma frigideira?")
resposta5 = input()
if resposta5 == "sim":
	contador += 1

if 0 <= contador <= 2:
	print("O culpado é ",suspeito1)
elif contador >= 3 and contador <= 4:
	print("O culpado é ",suspeito2)
elif contador == 5:
	print("O culpado é ",suspeito3)
else:
	print(suspeito1,suspeito2,suspeito3)

