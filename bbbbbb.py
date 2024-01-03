valor_avista = float(input())
quantidade = int(input())

valorAntes = (valor_avista + valor_avista*(0.1))

valorCerto = valorAntes/quantidade

prestacao = valorCerto -(valorCerto*(0.1))

valorDepois = prestacao*quantidade

print(valorAntes)
print(valorDepois)
