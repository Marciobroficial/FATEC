# 12. Faça um programa que receba três números obrigatoriamente em ordem crescente e um quarto número que não siga essa regra. Mostre, em seguida, os quatro números em ordem decrescente. Suponha que o usuário digitará quatro números diferentes.

# SE numero4 > numero3
#    ESCREVA “A ordem decrescente é: “,numero4,“-”,numero3,“-”,numero2,“-”,numero1
# SE numero4 > numero2 E numero4 < numero3
#    ESCREVA “A ordem decrescente é: “,numero3,“-”,numero4,“-”,numero2,“-”,numero1
# SE numero4 > numero1 E numero4 < numero2
#    ESCREVA “A ordem decrescente é: “,numero3,“-”,numero2,“-”,numero4, “-”,numero1
# SE numero4 < numero1
#    ESCREVA “A ordem decrescente é: “,numero3,“-”,numero2,“-”,numero1,“-”,numero4

# Primeiro resultado

# Double-click (or enter) to edit

# Segundo resultado

n1 = float (input ('Digite o 1º Numero: '))
n2 = float (input ('Digite o 2º Numero: '))
if  n2  >  n1 : # verifica se o primeiro número é menor que o segundo para continuar
    n3  =  float ( input ('Insira outro número maior que os dois anteriores: ')) #se o último passo for verdadeiro, ele executará esta parte
    if  n3  >  n2 : # verifica se o terceiro número é maior que o segundo para avançar para a última etapa de entrada
        n4  =  float ( input ('Insira qualquer número de sua escolha: ')) #se todas as outras condições forem verdadeiras, ele armazenará valor para o 4º número
        if  n4  >  n3 : # verifica se o quarto número é maior que o terceiro para gerar o resultado
            print ('A ordem decrescente é: {:.0f} - {:.0f} - {:.0f} - {:.0f}'.format ( n4 , n3 , n2 , n1 ))
        elif  n4  >  n2  and  n4 < n3 : # verifica se o 4º número é maior que o 2º e se é menor que o 3º para produzir o resultado
            print ('A ordem decrescente é: {:.0f} - {:.0f} - {:.0f} - {:.0f}'.format ( n3 , n4 , n2 , n1 ))
        elif  n4  >  n1  and  n4  <  n2 : # verifica se o quarto número é maior que o primeiro e se é menor que o segundo para produzir o resultado
            print ('A ordem decrescente é: {:.0f} - {:.0f} - {:.0f} - {:.0f}'.format ( n3 , n2 , n4 , n1 ))
        elif  n4  <  n1 : # verifica se o 4º número é menor do que o 1º inserido
            print ('A ordem decrescente é: {:.0f} - {:.0f} - {:.0f} - {:.0f}'.format ( n3 , n2 , n1 , n4 ))
        elif  n4  ==  n1  or  n4  ==  n2  or  n4  == n3 : # verifica se os valores do 4º número são iguais a qualquer um dos outros inseridos, para que finalize o programa com uma mensagem de que o usuário deve inserir um número maior
            print ('Este número não pode ser igual ao número digitado anteriormente!')
    else:
        print ('Este número precisa ser maior que o anterior!') # se n3 não for maior que n2, execute-o
else:
    print ('Este número precisa ser maior que o anterior!') # e n2 não for maior que n1, execute-o
