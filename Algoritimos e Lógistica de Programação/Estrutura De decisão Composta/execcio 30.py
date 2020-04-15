# 30. Faça um programa que receba de um produto:
# o preço
# o tipo (A — alimentação; L — limpeza; e V — vestuário)
# a refrigeração (S — produto que necessita de refrigeração; e N — produto que não necessita de refrigeração) .
# Suponha que haverá apenas a digitação de dados válidos e, quando houver digitação de letras, utilize maiúsculas.
# Calcule e mostre:

# O valor adicional, de acordo com a tabela a seguir:
# REFRIGERAÇÃO	TIPO	        PREÇO	VALOR ADICIONAL
#  N	 A	      < 15,00	      2,00
#              >= 15,00	      5,00
# ---------	---------------	-------- ----------------------
#  L	          < 10,00	      1,50
#              >= 10,00	      2,50
# ---------	---------------	-------- ----------------------
#  V          	< 30,00	      3,00
#              >= 30,00	      2,50
# --------- --------------- -------- ----------------------
#  S	A	                      8,00
#  L	                      	0,00
#  V		                      0,00
# --------- --------------- -------- ----------------------
# O valor do imposto, de acordo com a regra a seguir.
# PREÇO	      PERCENTUAL SOBRE O PREÇO
# < 25,00	    5%
# >= 25,00	  8%
#O preço de custo, ou seja, preço mais imposto. O desconto, de acordo com a regra a seguir.

# O produto que não preencher nenhum dos requisitos a seguir terá desconto de 3%, caso contrário, 0 (zero). Os requisitos são:

# Tipo: A

# Refrigeração: S

# O novo preço, ou seja, preço de custo mais adicional menos desconto.

# A classificação, de acordo com a regra a seguir.

# NOVO PREÇO	            CLASSIFICAÇÃO
# <= 50,00	              Barato
# Entre 50,00 e 100,00	  Normal
# >= 100,00	              Caro

# LEIA pre, tipo, refrig
# SE refrig = “N”
#     SE tipo = “A”
#         SE pre < 15
#           valor_adic = 2
#        SENÃO 
#           valor_adic = 5
#     SE tipo = “L”
#       SE pre < 10
#         valor_adic = 1.5
#       SENÃO 
#         valor_adic = 2.5
#     SE tipo = “V”
#       SE pre < 30
#         valor_adic = 3
#       SENÃO 
#         valor_adic = 2.5
# SENÃO SE tipo = “A”
#     valor_adic = 8
#   SE tipo = “L”
#     valor_adic = 0
#   SE tipo = “V”
#     valor_adic = 0
# ESCREVA valor_adic
# SE pre < 25
#   imposto = 5/100 * pré
# SENÃO 
#   imposto = 8/100 * pre
# ESCREVA imposto
# pre_custo = pre + imposto
# ESCREVA pre_custo
# SE tipo != “A” E refrig != “S”
#   desconto = 3/100 * pre_custo
# SENÃO 
#   desconto = 0
# ESCREVA desconto
# novo_pre = pre_custo + valor_adic – desconto
# ESCREVA novo_pre
# SE novo_pre <= 50
#   ESCREVA “Barato”
# SENÃO SE novo_pre < 100
#          ESCREVA “Normal”
#       SENÃO 
#          ESCREVA “Caro”
#######################################################################################################################
