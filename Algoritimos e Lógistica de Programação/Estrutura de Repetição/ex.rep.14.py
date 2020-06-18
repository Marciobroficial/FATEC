# 14. Um funcionário de uma empresa recebe, anualmente, aumento salarial.
# Sabe-se que:
#
# Esse funcionário foi contratado em 2005, com salário inicial de R$ 1.000,00.
# Em 2006, ele recebeu aumento de 1,5% sobre seu salário inicial.
# A partir de 2007, os aumentos salariais sempre corresponderam ao dobro do percentual do ano anterior.
# Faça um programa que determine o salário atual desse funcionário.
#
# LEIA ano_atual
# 
# salario_inicial =1000
# percentual_de_aumento_do_ano  = 1.5 / 100
#
# aumento_do_ano = salario_inicial * percentual_de_aumento_do_ano
# salario_do_ano = salario_inicial + aumento_do_ano
# 
# PARA ano NO INTERVALO DE 2007 ATÉ ano_atual + 1
#     percentual_do_ano = percentual_do_ano * 2
#     aumento_do_ano = salario_do_ano * percentual_do_ano
#     salario_do_ano = salario_do_ano + aumento_do_ano
# 
# ESCREVA ano, salario_do_ano
###########################################################################################################

anoAtual = int(input("Qual o ano atual? "))
si = 1000
perCentAnual = 1.5 / 100
aumento_do_ano = si * perCentAnual
salario_do_ano = si + aumento_do_ano
ano = 2007
while ano <= anoAtual:
    perCentAnual = perCentAnual * 2
    aumento_do_ano = salario_do_ano * perCentAnual
    salario_do_ano += aumento_do_ano
    ano += 1
print("O salário referente ao ano de {} é de R${:.2f} ".format(ano - 1, salario_do_ano))

# anoAtual = int(input("Qual o ano atual? "))
# si = 1000
# perCentAnual = 1.5 / 100
# aumento_do_ano = si * perCentAnual
# salario_do_ano = si + aumento_do_ano
#
# for ano in range(2007, anoAtual + 1):
#     perCentAnual = perCentAnual * 2
#     aumento_do_ano = salario_do_ano * perCentAnual
#     salario_do_ano += aumento_do_ano
# print("O salário referente ao ano de {} é de R${:.2f} ".format(ano, salario_do_ano))