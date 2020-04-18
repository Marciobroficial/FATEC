#####################################################################################################################
# 29. Faça um programa que: Receba o valor do salário mínimo,
# o turno de trabalho (M — matutino; V — vespertino; ou N — noturno),
# a categoria (O — operário; G — gerente)
# número de horas trabalhadas no mês de um funcionário.
# Suponha a digitação apenas de dados válidos e, quando houver digitação de letras, utilize maiúsculas.
#
#   Calcule e mostre:
#
#   O coeficiente do salário, de acordo com a tabela a seguir.
#
#       TURNO DE TRABALHO	    VALOR DO COEFICIENTE
#       M - Matutino	        10% do salário mínimo
#       V - Vespertino	        15% do salário mínimo
#       N - Noturno	            20% do salário mínimo
#
#   O valor do salário bruto, ou seja, o número de horas trabalhadas multiplicado pelo valor do coeficiente do salário.
#
#   O imposto, de acordo com a tabela a seguir.
#
#       CATEGORIA	        SALÁRIO BRUTO	IMPOSTO SOBRE O SALÁRIO BRUTO
#       O - Operário	    >= 300,00	    5%
#       O - Operário	    <  400,00	    3%
#       G - Gerente	        >= 300,00	    6%
#       G - Gerente	        <  400,00	    4%
#
# A gratificação, de acordo com as regras a seguir. Se o funcionário preencher todos os requisitos a seguir, sua gratificação # será de 50,00; caso contrário, será de 30,00. Os requisitos são:
# Turno: Noturno
# Número de horas trabalhadas: Superior a 80 horas
# O auxílio alimentação, de acordo com as seguintes regras.
# Auxilio alimentação, um terço do seu salário bruto; caso contrário, será de metade do seu salário bruto. Os requisitos são:
# Se o funcionário preencher algum dos requisitos a seguir, seu auxílio alimentação será de
#
#           Categoria:                 Operário
#           Coeficiente do salário:    < = 25
#
# O salário líquido, ou seja, salário bruto menos imposto mais gratificação mais auxílio alimentação.
# A classificação, de acordo com a tabela a seguir:
#
#           SALÁRIO LÍQUIDO	        MENSAGEM
#           Menor que 350,00	    Mal remunerado
#           Entre 350 e 600,00	    Normal
#           Maior que 600,00	    Bem remunerado
#
# LEIA salario_minino, turno, categoria, numero_de_horas_trabalhadas
# SE turno = “M”
#      coeficiente = 10/100 * salario_minino
# SE turno = “V”
#      coeficiente = 15/100 * salario_minino
# SE turno = “N”
#      coeficiente = 12/100 * salario_minino
#
# ESCREVA coeficiente
# 
# salario_bruto = numero_de_horas_trabalhadas * coeficiente
# 
# ESCREVA salario_bruto
# 
# SE categoria = “O”
#     SE sal_bruto >= 300
#         imposto = 5/100 * sal_bruto
#     SENÃO
#         imposto = 3/100 * sal_bruto
# SENÃO
#     SE salario_bruto >= 400
#         imposto = 6/100 * salario_bruto
#     SENÃO
#          imposto = 4/100 * salario_bruto
#
# ESCREVA imposto
# 
# SE turno = “N” E numero_de_horas_trabalhadas > 80
#     gratificacao = 50
# SENÃO
#     gratificacao = 30
# 
# ESCREVA gratificacao
# 
# SE categoria = “O” OU coeficiente <= 25
#     auxilio = 1/3 * salario_bruto
# SENÃO
#    auxilio = 1/2 * salario_bruto
# 
# ESCREVA auxilio
# 
# salario_liquido = salario_bruto – imposto + gratificacao + auxilio
# 
# ESCREVA salario_liquido
# 
# SE salario_liquido < 350
#      ESCREVA “Mal Remunerado”
# SE salario_liquido >= 350 E salario_liqquido <= 600
#     ESCREVA “Normal”
# SE salario_liquido > 600
#      ESCREVA “Bem Remunerado”
########################################################################################################################
print ('<->' *35)
salário = float ( input ( '\nDigite seu salário mínimo :> ' ))
turno = int ( input ( 'Em que período do dia você trabalha?\n Digite (M) para Matutino, \n(v) para Vespertino e \n(N) para Noturno :>' ))
category  =  int ( input ( 'Qual é a sua categoria na empresa? Digite O para OPERATOR ou M para MANAGER :> ' ))
hours_worked  =  float ( input ( 'Digite o número de horas trabalhadas pelo funcionário durante o mês :> ' ))

if turno == "M" :
    coeficiente = salário * 10 / 100
elif turno == "A" :
    coeficiente  = salário * 15 / 20
elif turno == "N":
    coeficiente  = salário * 20 / 100
print ( 'O coeficiente do salário é: {}' .format ( coeficiente ))

sal_bruto = horas_trabalhadas  * coeficiente
print ( "O salário bruto é: {}" .format ( sal_bruto ))

if categoria  ==  "O" :
    if sal_bruto >= 300:
        impostos = sal_bruto * 5 / 100
    else :
        imposto = sal_bruto * 3 / 100
else:
    if sal_bruto >= 400:
        imposto  =  sal_bruto  *  6  /  100
    else:
        imposto  =  sal_bruto  *  4  /  100
print ( "O imposto a ser pago com base no salário bruto é: {}" . formato ( imposto ))
if  turno  ==  "N"  and  hours_worked  >  80 :
     bônus = 50
else:
     bônus = 30
print ( "O bônus calculado para esse funcionário com base em suas horas trabalhadas e turno é: {}" . formato ( bônus ))
if  categoria  ==  "O"  or  coeficiente <= 25 :
    assistência  =  sal_bruto  * 1 / 3
else:
    assistência  =  sal_bruto  *  1  / 2
print ( "A assistência que você terá é: {}" .format ( assistência ))
net_wages  =  salário bruto  -  imposto  +  bônus  +  assistência
print ( "Seu salário líquido é: R$ {}" .format ( net_wages ))
if net_wages  <  350 :
    print ( "Você é mal pago." )
elif net_wages >= 350  and net_wages <= 600:
    print ( "Você tem salário está bem" )
else:
    print ( "Você é bem pago" )