# 21. Faça um programa que receba o valor do salário mínimo, o número de horas trabalhadas,
# o número de dependentes do funcionário e a quantidade de horas extras trabalhadas.
# Calcule e mostre o salário a receber do funcionário de acordo com as regras a seguir:

# O valor da hora trabalhada é igual a 1/5 do salário mínimo.
# O salário do mês é igual ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada.
# Para cada dependente, acrescentar 32,00.
# Para cada hora extra trabalhada, calcular o valor da hora * trabalhada acrescida de 50%.
# O salário bruto é igual ao salário do mês mais o valor dos dependentes mais o valor das horas extras.
# Calcular o valor do impostoosto de renda retido na fonte de acordo com a tabela a seguir:

# IRFF	    SALÁRIO BRUTO
# Isento	Inferior a 200,00
# 10%	    De 200,00 até 500,00
# 20%	    Superior a 500,00

# O salário líquido é igual ao salário bruto menos IRRF.
# A gratificação é de acordo com a tabela a seguir:

# SALÁRIO LÍQUIDO	  GRATIFICAÇÃO
# Até 350,00	      100,00
# Superior a 350	  50,00

# O salário a receber do funcionário é igual ao salário líquido mais a gratificação.

# LEIA salario_minimo, numero_de_horas_trabalhadas, numero_de_dependentes, numero_de_horas_extras
 
# valor_da_hora = 1/5 * salario_minimo
# salario_do_mes = numero_de_horas_trabalhadas * valor_da_hora
# valor_dos_dependentes = 32 * numero_de_dependentes
# valor_da_hora_extra = numero_de_horas_extras * (valor_da_hora + (valor_da_hora * 50/100))
# salario_bruto =salario_do_mes + valor_dos_dependentes + valor_da_hora_extra
 
# SE salario_bruto < 200
#    ENTÃO imposto = 0
# SE salario_bruto >= 200 E salario_bruto <= 500
#   ENTÃO imposto = salario_bruto * 10/100
# SE salario_bruto > 500
#   ENTÃO imposto = salario_bruto * 20/100
# salario_liquido = salario_bruto – imposto
# SE salario_liquido <= 350
#    ENTÃO gratificacao = 100
# SE salario_liquido > 350
#    ENTÃO gratificacao = 50
# salario_a_receber = salario_liquido + gratificacao
 
# ESCREVA salario_a_receber
##################################################################################################################