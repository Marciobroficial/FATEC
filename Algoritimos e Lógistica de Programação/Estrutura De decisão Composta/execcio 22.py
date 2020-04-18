# 22 Um supermercado deseja reajustar os preços de seus produtos usando o seguinte critério:
# o produto poderá ter seu preço aumentado ou diminuído. Para o preço ser alterado,
# o produto deve preencher pelo menos um dos requisitos a seguir:
#
# VENDA MÉDIA MENSAL	PREÇO ATUAL	% DE AUMENTO	% DE DIMINUIÇÃO
# < 500	< 30.000	         10	-
# >= 500 e <1.200	> = 30,00 e < 80,00	15	-
# >= 1,200	> = 80,00	-	20
#
# Faça um programa que receba o preço atual e a venda média mensal do produto, calcule e mostre o novo preço.
#
# LEIA preco_atual, media_mensal_de_vendas
#
# SE media_mensal_de_vendas < 500 OU preco_atual < 30
#    novo_preco = preco_atual + 10/100 * preco_atual
# SENÃO SE media_mensal_de_vendas >= 500 E media_mensal_de_vendas < 1200 OU preco_atual >= 30 E preco_atual<80
#    ENTÃO novo_preco = preco_atual + 15 / 100 * preco_atual
# SENÃO SE venda >= 1200 OU preco_atual >= 80
#    ENTÃO novo_preco = preco_atual – 20 / 100 * preco_atual
# 
# ESCREVA novo_preco
#
#########################################################################################################################
print ('<->' *35)
preço_atual  =  float ( input ( '\nQual é o preço atual do produto? R$: ' ))
m_mensal  =  int ( input ( 'Qual foi o número médio de vendas deste produto: ' ))

if  m_mensal  < 500 or preço_atual < 30 :
    novo_preço =  preço_atual + ( preço_atual  * 10  / 100 )
elif  m_mensal >= 500 and m_mensal < 1200  or  preço_atual >= 30 and preço_atual < 80 :
    novo_preço = preço_atual + ( preço_atual  *  15  /  100 )
elif  m_mensal >= 1200 or preço_atual  >=  80 :
    novo_preço = preço_atual -( preço_atual * 20 / 100 )

print ( 'O novo preço do produto é: R$ {}\n' .format ( novo_preço ))
print ('<->' *35)
