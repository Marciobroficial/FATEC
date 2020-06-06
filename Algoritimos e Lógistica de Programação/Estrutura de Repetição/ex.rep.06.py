# 6. Faça um algoritmo que receba a idade de 10 pessoas,
# calcule e exiba a quantidade de pessoas maiores de idade,
# sendo que a maioridade é obtida após completar 18 anos.
###############################################################

maior = 0
menor = 0
for a in range (10):
    idade = int (input ('Digite a idade: '))
    if idade >= 18:
        maior = maior +1
    else:
        menor = menor +1
print("Temos",maior, "maior de idade: " )
print("E ",menor, "de idade: ") 

