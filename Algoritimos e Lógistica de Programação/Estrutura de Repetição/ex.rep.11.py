
#
# 11. Construir um algoritmo para calcular a média aritmética de preços de 5 produtos.

######################################################################################

# soma = 0
# c = 1
# while c <= 5:
#     p = float(input("Qual o preço do produto n° {} -> ".format(c)))
#     soma += p
#     c += 1
# media = soma / 5
# print("A média de preço dos produtos é R${:.2f}".format(media))

soma = 0
for c in range(1, 6):
    p = float(input("Qual o preço do produto n° {} -> ".format(c)))
    soma += p
media = soma / 5
print("A média de preço dos produtos é R$: {:.2f}".format(media))