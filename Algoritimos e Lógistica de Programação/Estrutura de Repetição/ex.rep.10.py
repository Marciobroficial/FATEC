# 10. Elabore um algoritmo que calcule e informe a média de idades de 5 alunos.

################################################################################

# soma = 0
# c = 1
# while c <= 5:
#     i = int(input("Digite a idade do aluno n° {} -> ".format(c)))
#     soma += i
#     c += 1
# media = soma / 5
# print("A média da idade dos alunos é {}".format(media))

soma = 0
for c in range(1, 6):
    i = int(input("Digite a idade do aluno n° {} -> ".format(c)))
    soma += i
media = soma / 5
print("A média de idade dos alunos é {}".format(media))