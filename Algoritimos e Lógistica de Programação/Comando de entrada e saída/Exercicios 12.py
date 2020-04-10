 #Faça um programa que receba dois números maiores que zero, calcule e mostre um elevado ao outro.
  #LEIA numero1, numero2
  #numero1_elevado_numero2 = numero1 ** numero2
  #numero2_elevado_numero1 = numero2 ** numero1
  #ESCREVA numero1_elevado_numero2, numero2_elevado_numero1

#Entrada de dados

numero1 = float (input('Digite o valor positivo a ser calculado: '))

numero2 = float (input('Digite o valor positivo a ser calculado: '))

#Processamento

n1_e_n2 = numero1 ** numero2

n2_e_n1 = numero2 ** numero1

#Saida de dados

print ('O numero 1 elevado numero 2 é: ', n1_e_n2)

print ('O numero 2 elevado numero 1 é: ', n2_e_n1)