#####################################################################################################################
# 26. Faça um programa que receba:
# O código de um produto comprado, supondo que a digitação do código
# do produto seja sempre válida, isto é, um número * inteiro entre 1 e 10.
# O peso do produto em quilos.
# O código do país de origem, supondo que a digitação
# do código seja sempre válida, isto é, um número inteiro entre 1 e 3.
#
#   CÓDIGO DO PAÍS DE ORIGEM	IMPOSTO
#   1 ------------------------- 0%
#   2 ------------------------- 15%
#   3 ------------------------- 25%
#
#   CÓDIGO DO PRODUTO	        IMPOSTO
#   1 a 4  -------------------- 10
#   5 a 7  -------------------- 25
#   8 a 10 -------------------- 35
#
# Calcule e mostre:
#
# o peso do produto convertido em gramas;
# o preço total do produto comprado;
# valor do imposto, sabendo que ele é cobrado sobre
# o * preço total do produto comprado e dependendo país de origem;
# o valor total, preço total do produto mais imposto.
#
# LEIA codigo_do_produto, peso_quilos, codigo_do_paiz
# peso_em_gramas = peso_quilos * 1000
#
# ESCREVA peso_em_gramas
# SE codigo_do_produto >= 1 E codigo_do_produto <= 4
#    preco_por_grama = 10
# SE codigo_do_produto >= 5 E codigo_do_produto <= 7
#    preco_por_grama = 25
# SE codigo_do_produto >= 8 E codigo_do_produto <= 10
#    preco_por_grama = 35    
# preco_total = peso_em_gramas *preco_por_grama
# ESCREVA preco_total
# SE codigo_do_paiz = 1
#    imposto = 0
# SE codigo_do_paiz = 2
#    imposto = preco_total * 15/100
# SE codigo_do_paiz = 3
#    imposto = preco_total * 25/100    
# ESCREVA imposto
# valor_total = preco_total + imposto
# ESCREVA valor_total
######################################################################################################################
print ('<->' *35)
print()
print ( 'Menu de opções:\n\nCod - 01 a 04 Imposto 10% \nCod - 05 a 07 Imposto 20% \nCod - 08 a 10 Imposto 35% ' )
cod_produto  =  int ( input ( "\nQual é o código do produto? :> " ))
peso_por_kilo  =  float ( input ( "Qual é o peso do produto? Use (K.GM) :> " ))
print()
print ( 'Menu de opções:\n\nCod - 1 Imposto 0% \nCod - 2 Imposto 15% \nCod - 3 Imposto 25% ' )
cod_produto  =  int ( input ( "\nDigite o código do país: " ))
peso_por_gramas = peso_por_kilo * 1000
print ( 'O peso em gramas é: {}\n' .format ( peso_por_gramas ))
if  cod_produto >= 1 and cod_produto <= 4:
    preço_por_grama = 10
if  cod_produto >= 5 and cod_produto <= 7:
    preço_por_grama = 25
if  cod_produto >= 8 and cod_produto <= 10:
    preço_por_grama = 35
preço_total = peso_por_gramas * preço_por_grama
print ( 'O preço final do produto é: {}\n' .format ( preço_total) )
if  cod_produto == 1:
    impostos  =  0
if  cod_produto == 2:
    impostos = preço_total * 15 / 100
if  cod_produto == 3:
    impostos = preço_total * 25 / 100
print ( 'O imposto cobrado é: {}\n' .format ( impostos ))
valor_final = preço_total + impostos
print ( 'Após a cobrança do impostos o valor é: {}\n' .format ( valor_final ))
print ('<->' *35)