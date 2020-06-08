# 8. Faça um algoritmo que calcule e exiba o salário 
# reajustado de dez funcionários de acordo com a seguinte regra:
# Salário até 300, reajuste de 50%;

# Salários maiores que 300, reajuste de 30%.
############################################################################

c = 1
print("Informe o salário dos 10 funcionários abaixo: ")
while c <= 10:
    s = float(input("Salário {} -> ".format(c)))
    c += 1
    if s > 0 and s <= 300:
        ns = s + s * (50 / 100)
        print(ns)
    else:
        ns = s + s * (30 / 100)
        print(ns)


# print("Informe o salário dos 10 funcionários abaixo: ")
# for c in range(1, 11):
#     s = float(input("Salário {} -> ".format(c)))
#     if s > 0 and s <= 300:
#         ns = s + s * (50 / 100)
#         print(ns)
#     else:
#         ns = s + s * (30 / 100)
#         print(ns)