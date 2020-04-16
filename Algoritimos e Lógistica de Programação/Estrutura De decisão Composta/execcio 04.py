###################################################################################################
# 4. Faça um algoritmo que leia um número inteiro e mostre uma
# mensagem indicando se este número é par ou ímpar e se é positivo ou negativo.
###################################################################################################

# Entrada
n = int (input('Digite um numero inteiro: '))

# Procedimento
if  n >= 0:
    print ('Este numero é positivo')
else:
    print ('Este numero negativo')
if n %2 == 0:
    print ("Este numero é par")    
else:
    print ('Este numero é impar')    
######################################################################################################
