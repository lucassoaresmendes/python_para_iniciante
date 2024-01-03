"""
Função que acessa  o dispositivo de entrada padrão
input()
variavel = input("Mensagem a ser exibida (opcional)")

Funções
(class 'int') => int()
(class 'float') => float()
(class 'str') => str
(class 'bool') => bool()
"""

numeroTexto = input("Digite um numero qualquer: ")#De forma mais prática para converte pode-se fazer int(input("Digite um número qualquer"))
numeroInteiro = int(numeroTexto)
print("O numero digitado foi:", numeroInteiro)

"""
Sintaxe para importação biblioteca
from nome_biblioteca import nome_funcao

from math import sqrt

funcoes
sqrt - raiz
cos
sin
tan
ceil - arredondamento para cima
floor - arredondamento para baixo

"""
