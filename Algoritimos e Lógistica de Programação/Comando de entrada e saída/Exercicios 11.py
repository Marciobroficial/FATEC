#Faça um programa que receba um número positivo e maior que zero, calcule e mostre:

#O número digitado ao quadrado

#O número digitado ao cubo

#A raiz do número digitado

#A raiz cúbica do número digitao

#LEIA numero
#quadrado = numero ** 2
#cubo = numero ** 3
#raiz_quadrada = numero ** ½ (elevado a meio)
#raiz_cubica = numero ** ⅓ (elevado ao um terço)
#ESCREVA quadrado, cubo, raiz_quadrada, raiz_cubica


#Entrada de dados
numero = float (input('Digite o valor positivo a ser calculado: '))

#Processamento

quadrado = numero ** 2

cubo = numero ** 3

raiz_quadrada = numero ** (1/2)

raiz_cubica = numero ** (1/3)

#Saida de dados

print ('O quadrado é: ',quadrado)
print ('O valor cubico é: ',cubo)
print ('O valor rais quandrada é: ',raiz_quadrada)
print ('o valor rais cubica é: ',raiz_cubica )