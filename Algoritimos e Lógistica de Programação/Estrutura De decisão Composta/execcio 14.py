#############################################################################################################
# 14. Faça um programa que mostre o menu de opções a seguir,receba a opção do usuário
#  e os dados necessários para executar cada operação.
# Menu de opções:
# 1. Somar dois números.
# 1. Raiz quadrada de um número.
#
# Digite a opção desejada:
# raiz = numero ** (1/2)
##############################################################################################################
print('<->'*35)
print()
from  math  import  sqrt
print ( 'Menu de opções: \n1º Adicione dois números. \n2º A raiz quadrada de um número.' ) 
opção  =  int ( input ( '\nEscolha uma das opções do menu: ' ))
if  opção  ==  1 : 
    n1  =  int ( input ( 'Digite o primeiro número: ' ))
    n2  =  int ( input ( 'Digite o segundo número para adicionar os dois: ' ))
    print ( 'A soma de {} e {} é {}' .format ( n1 , n2 , n1  +  n2 ))
    print()
    print ('=' *35)
elif opção ==  2 : 
    n  =  int ( input ( 'Digite um número para saber sua raiz quadrada: ' ))
    print ( 'A raiz quadrada de {} é {}' .format ( n , sqrt ( n )))
    print()
    print ('=' *35)
else :
    print ( 'opção inválida' )
    print()
    print ('=' *35)