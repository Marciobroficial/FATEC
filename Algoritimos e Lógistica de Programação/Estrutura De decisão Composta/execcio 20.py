######################################################################################################################
# 20. Faça um programa que receba o salário inicial de um funcionário,
# calcule e mostre o novo salário, acrescido de bonificação e de auxílio escola.

# SALÁRIO	                    BONIFICAÇÃO
# Até 500,00	                5% do salário
# Entre 500,00 e 1.200,00	    12% do salário
# Acima de 1.200,00	            Sem bonificação

# SALÁRIO	        AUXÍLIO ESCOLA
# Até 600,00	    150,00
# Acima de 600,00	100,00

# novo_salario = salario + bonificacao + aux
#####################################################################################################################
print ( '<->'  *  44 )
salario = float (input ('Informe o seu Salario atual: R$: '))
if  salario < 500:
            bonus : float = salario * 5 / 100
elif salario >= 500 and salario <= 1.200 :
            estra = salario * 12 / 100
elif salario > 1200 :
            estra = 0       
if salario > 0 and salario <= 600:
    aux_salario = 150
else:
    aux_salario = 100
print('Seu Novo salário com estra e Auxilio Escolar será de R$: {:.2f}'.format ( salario +  estra + aux_salario ))   