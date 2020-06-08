
# 1. Faça um algoritmo que mostre 10 vezes a frase “Bem vindo a Fatec!”.
#########################################################################################################

print('-'*20)
frase = 1
while frase <= 10:
    print ("Bem-vindo à FATEC!") #<modelo wile>
    frase += 1
    
print('-'*20)

for contador in range(1,11):
    print("Bem-vindo à FATEC!".format(contador)) #<modelo for>
print('-'*20)