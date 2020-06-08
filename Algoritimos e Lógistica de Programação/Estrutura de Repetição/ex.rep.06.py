# 6. Faça um algoritmo que receba a idade de 10 pessoas,
# calcule e exiba a quantidade de pessoas maiores de idade,
# sendo que a maioridade é obtida após completar 18 anos.
###############################################################

maiores = 0
menores = 0
for b in range (10):
    idade = int(input("Digite a idade: "))
    if idade >= 18:
        maiores =maiores + 1
    else:
        menores = menores + 1
print ("São de maior idade: ",maiores) 
print ("São de menor idade: ",menores)           

