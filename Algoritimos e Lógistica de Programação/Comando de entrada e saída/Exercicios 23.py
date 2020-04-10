#23. Faça um programa que receba um número real, encontre e mostre:
#a parte inteira desse número; a parte fracionária desse número; o arredondamento desse número.

#Observação: Para arredondar um número em Python, usa-se a função round(numero), onde 
# se o número real/float estiver em igual distância
# entre o inteiro de cima e o inteiro de baixo,
# esta função arredonda para o número par mais próximo.

#LEIA numero
#parte_inteira = numero // 1
#parte_fracionaria = numero - parte_inteira
#numero_arredondado = arredonda (numero)

#ESCREVA parte_inteira
#ESCREVA parte_fracionaria
#ESCREVA numero_arredondado

#Entrada
num = float (input ("informe o numro interio: "))

#Procedimento
parte_int = num // 1

parte_frac = num - parte_int

parte_arredondado = round (num) 

#Saída
print ("A parte interia é: ",parte_int)
print ("A parte fracionaria é: ",parte_frac)
print ("A parte arredondada é: ",parte_arredondado)