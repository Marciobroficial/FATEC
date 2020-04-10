# 14. Faça um programa que mostre o menu de opções a seguir,receba a opção do usuário
#  e os dados necessários para executar cada operação.
# Menu de opções:
# 1. Somar dois números.
# 1. Raiz quadrada de um número.
 
# Digite a opção desejada:
# raiz = numero ** (1/2)
##############################################################################################################

from  math  import  sqrt  #library para fazer raiz quadrada automaticamente
print ( "="  *  27 ) #lines 8, 9 e 10 cria o menu
print ( "Menu de opções: \ n 1. Adicione dois números. \ n 2. A raiz quadrada de um número." ) # \ n é estrelar uma nova linha sem ter outro comando de impressão
print ( "="  *  27 )
option  =  int ( input ( "Digite uma das opções do menu ->" )) #user seleciona a opção no menu
if and  opção  ==  1 : #se o usuário digitar a opção 1, o programa obtém a soma dos dois números inseridos e a imprime
    n1  =  int ( input ( "Digite o primeiro número:" ))
    n2  =  int ( input ( "Digite o segundo número para adicionar os dois:" ))
    print ( "A soma de {} e {} é {}" . formato ( n1 , n2 , n1  +  n2 ))
 opção  elif ==  2 : #se o usuário escolher essa ação, ela obtém a raiz quadrada do número digitado e a imprime
    n  =  int ( input ( "Digite um número para saber sua raiz quadrada:" ))
    print ( "A raiz quadrada de {} é {}" . formato ( n , sqrt ( n )))
else : #tells ao usuário que é uma opção inválida
    print ( "opção inválida" )