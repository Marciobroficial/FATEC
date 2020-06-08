#
# 7. Escreva um algoritmo que receba 23 números, calcule e exiba a quantidade de números pares e impares.
############################################################################################################

p = 0
i = 0
for r in range (23):
    n = int(input("Digite o numero: "))
    if n >= 23:




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