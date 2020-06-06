
# 1. Faça um algoritmo que mostre 10 vezes a frase “Bem vindo a Fatec!”.
#########################################################################################################

frase = 1
while frase <= 10:
    print ("Bem-vindo à FATEC!")
    frase += 1
print()
for contador in range(1,11):
    print("Bem-vindo à FATEC!".format(contador))
