##############################################################################################################################
# 19. Faça um programa que apresente o menu a seguir, permita ao usuário escolher a opção desejada,
# receba os dados necessários para executar a operação e mostre o resultado.
# Verifique a possibilidade de opção inválida e não se preocupe com restrições, como salário negativo.
#
#   Menu de opções
#   1. Imposto
#   2. Novo salário
#   3. Classificação
#   Digite a opção desejada:
# Na opção 1: receber o salário de um funcionário, calcular e mostrar o valor do imposto usando as regras a seguir.
#
#   SALÁRIO	                                        PERCENTUAL DO IMPOSTO
#   Menor que 500,00	                             5%
#   De 500,00 (inclusive) a 850,00 (inclusive)	    10%
#   Acima de 850,00	                                15%
# Na opção 2: receber o salário de um funcionário, calcular e mostrar o valor do novo salário, usando as regras a seguir.
#
#   SALÁRIO	                                            AUMENTO
#   Maior que 1.500,00	                                 25,00
#   De 750,00 (inclusive) a 1.500,00 (inclusive)	     50,00
#   De 450,00 (inclusive) a 750,00	                     75,00
#   Menor que 450,00	                                100,00
#
# Na opção 3: receber o salário de um funcionário e mostrar sua classificação usando a tabela a seguir.
#
#   SALÁRIO	                    CLASSIFICAÇÃO
#   Até 700,00 (inclusive)      Mal remunerado
#   Maiores que 700,00	        Bem remunerado
#############################################################################################################################
print ('<->'*35)
print()
print ( 'Menu de opções: \nnº 1. Imposto \nnº 2. Novo salário \nnº 3. Classificação do salário' )
opção  =  int ( input ( 'Digite uma das opções do menu: ' ))
print()
salario  =  int ( input ( 'Qual é o seu salário atual ?. R$: ' ))
if  opção == 1 :
    if  salario < 500 :
        impostos = salario * 5 / 100
        print ( 'O imposto que você terá que pagar com base em seus salario é: R$ {: .2f}' .format ( impostos ))
    elif salario >= 500  and  salario <=  850 :
        impostos  = salario  *  10  /  100
        print ( 'O imposto que você terá que pagar com base em seus salario é: R$ {: .2f}' .format ( impostos ))
    elif salario > 850 :
        impostos  = salario  *  15  /  100
        print ( 'O imposto que você terá que pagar com base em seus salario é: R$ {: .2f}' .format ( impostos ))

elif opção == 2 :
        if  salario  < 450 :
            print ( 'Seu novo salário é de R$ {}' .format ( salario  +  100 ))
        elif salario >= 450  and  salario  <  750 :
            print ( "Seu novo salário é de R$ {}" .format ( salario  +  75 ))
        elif salario >=  750  and  salario  <=  1500 :
            print ( "Seu novo salário é de R$ {}" .format ( salario  +  50 ))
        elif salario >  1500 :
            print ( "Seu novo salário é de R$ {}" .format ( salario  +  25 ))

elif opção == 3 :
        if salario <= 700 :
                print ( "Você é Mal remunerado." )
        elif salario > 700 :
                print ( "Você é Bem remunerado." )
else :
    print ( "Opção inválida!" )
print()
print('<->'*35)
