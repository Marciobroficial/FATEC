# 27. Faça um programa que receba:
# o código do estado de origem da carga de um caminhão,
# supondo que a digitação do código do estado seja sempre válida, isto é, um número inteiro entre 1 e 5;
# o peso da carga do caminhão em toneladas;
# o código da carga, supondo que a digitação do código seja sempre válida, isto é, um número inteiro entre 10 e 40.

#       CÓDIGO DO ESTADO	    IMPOSTO
#       1	-- - - - - - - - -- 35%
#       2	-- - - - - - - - -- 25%
#       3	-- - - - - - - - -- 15%
#       4   -- - - - - - - - -- 05%
#       5	-- - - - - - - - -- Isento

#   CÓDIGO DA CARGA	            PREÇO POR QUILO
#   10 a 20 -- - - - - - - - -- 100
#   21 a 30 -- - - - - - - - -- 250
#   31 a 40 -- - - - - - - - -- 400

#   Calcule e mostre:

#   o peso da carga do caminhão convertido em quilos;
#   o preço da carga do caminhão;
#   o valor do imposto, sabendo que o imposto é cobrado sobre o preço da carga do caminhão e depende do estado de origem;
#   o valor total transportado pelo caminhão, preço da carga mais imposto.

#   LEIA codigo_do_estado, peso_em_toneladas, codigo_da_carga
#   peso_em_quilos = peso_em_toneladas * 1000

# ESCREVA peso_em_quilos
# SE cod_carga >= 10 E cod_carga <= 20
#     preco_da_carga = 100 * peso_em_quilos
# SE cod_carga >= 21 E cod_carga <= 30
#     preco_da_carga = 250 * peso_em_quilos
# SE cod_carga >= 31 E cod_carga <= 40
#     preco_da_carga = 340 * peso_em_quilos   
# ESCREVA preco_da_carga
# SE codigo_do_estado = 1
#     imposto = 35/100 * preco_da_carga
# SE cod_est = 2
#     imposto = 25/100 * preco_da_carga
# SE cod_est = 3
#     imposto = 15/100 * preco_ds_carga
# SE cod_est = 4
#     imposto = 5/100 * preco_da_carga
# SE cod_est = 5
#     imposto = 0
# ESCREVA imposto
# valor_total = preco_da_carga + imposto
# ESCREVA valor_total
#############################################################################################################################
print ('<->' *35)
cod_estado = int ( input ( '\nDigite o código do estado: ' ))
peso_em_toneladas = float ( input ( 'Informe o peso que o caminhão está carregando em toneladas :> ' ))
cod_garga = int ( input ( 'Qual é o código da carga do caminhão? :> ' ))

peso_em_quilos  =  peso_em_toneladas  *  1000
print ( '\nO peso em quilos é: {}' .format ( peso_em_quilos ))
if  cod_garga  >=  10  and  cod_garga  <=  20 :
    preço_carga =  100  *  peso_em_quilos
if  cod_garga  >=  21  and cod_garga  <=  30 :
    preço_carga =  250  *  peso_em_quilos
if  cod_garga  >=  31  and  cod_garga  <=  40 :
    preço_carga =  340  *  peso_em_quilos
print ( 'O preço da carga é: {: .2f}\n' .format ( preço_carga ))
if  cod_estado ==  1:
    impostos = preço_carga * 35 / 100
if  cod_estado ==  2:
    impostos = preço_carga * 25 / 100
if  cod_estado ==  3:
    impostos = preço_carga * 15 / 100
if  cod_estado ==  4:
    impostos = preço_carga * 5  / 100
if  cod_estado ==  5:
    impostos = 0
print ( 'O imposto cobrado é: {: .2f}' .format ( impostos ))
preço_final = preço_carga + impostos
print ( 'O preço líquido da carga após a cobrança de impostos é: {:.2f}\n' .format ( preço_final ))
print ('<->' *35)