#####################################################################################################################
# 28.Faça um programa que receba o salário base e o tempo de serviço de um funcionário.
# Calcule e mostre:
# O imposto, conforme a tabela a seguir.
# A gratificação, de acordo com a tabela a seguir.
# O salário líquido, ou seja, salário base menos imposto mais gratificação.
# A categoria, que está na tabela a seguir.
#
#   LEIA salario_base, tempo 
#   SE salario_base < 200
#       imposto = 0
#   SENÃO SE salario_base <= 450
#        imposto = 3/100 * salario_base
#   SENÃO SE sal_base < 700
#       imposto = 8/100 * salario_base
#   SENÃO
#       imposto = 12/100 * salario_base
#   ESCREVA imposto
#   SE salario_base > 500
#       SE tempo <= 3
#            gratificacao = 20
#       SENÃO 
#           gratificacao = 30
#   SENÃO
#      SE tempo <= 3
#         gratificacao = 23
#       SENÃO SE tempo < 6
#          gratificacao = 35
#       SENÃO gratificacao = 33
#   ESCREVA gratificacao
#   salario_liquido = salario_base – imposto + gratificacao
#   ESCREVA salario_liqquido
#   SE salario_liquido <= 350
#      ESCREVA “Classificação A”
#   SENÃO
#       SE salario_liqquido < 600
#           ESCREVA “Classificação B”
#       SENÃO
#           ESCREVA “Classificação C”
#######################################################################################################################
print ('<->' *35)
salário = float ( input ( '\nDigite seu salário base R$ ' ))
tempo  =  int ( input ( 'Agora digite o número de anos em que você trabalhou nesta empresa :> ' ))
if  salário < 200:
     imposto = 0
elif salário <= 450:
    imposto  =  salário * 3 / 100
elif salário < 700 :
    impostos = salário * 8 / 100
else:
    impostos = salário * 12 / 100
print ( '\nO imposto para esse salário é: R$ {}' .format ( imposto ))

if  salário > 500:
    if tempo <= 3:
        bônus = 20
    else:
        bônus = 30
else:
    if tempo <=  3:
        bônus  = 23
    elif tempo < 6:
       bônus  =  35
    else:
     bônus = 33
print ( 'O valor do bônus a ser recebido é: R$ {: .2f}\n'.format ( bônus ))
s_líquidos  =  salário  -  imposto  +  bônus
print ( "Seu salário líquido é: R$ {: .2f}" .format ( s_líquidos ))
if  s_líquidos  <=  350 :
    print ( 'Você está classificado como A\n' )
elif s_líquidos <  600 :
    print ( 'Você está classificado como B\n' )
else:
    print ( 'Você está classificado como C\n' )
print ('<->' *35)   
## 