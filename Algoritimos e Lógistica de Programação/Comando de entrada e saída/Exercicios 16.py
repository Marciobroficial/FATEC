#16. Faça um programa que receba o número de horas trabalhadas e o valor do salário mínimo,
#  calcule e mostre o salário a receber, seguindo estas regras:
#a hora trabalhada vale a metade do salário mínimo.
#o salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada.
#o imposto equivale a 3% do salário bruto.
#o salário a receber equivale ao salário bruto menos o imposto.

#LEIA quantidade_de_horas_trabalhadas
#LEIA valor_do_salario_minimo

#valor_hora_trabalhada = valor_do_salario_minimo / 2
#valor_salario_bruto = valor_da_hora_trabalhada *
#quantidade_de_horas_trabalhadas
#impostos = valor_salario_bruto * 3 / 100
#Valor_salario_liquido =  ← valor_salario_bruto - impostos
#ESCREVA valor_salario_liquido

#Entrada
Horas_trab = float (input("Digite as horas trabalhadas: "))

Salario_mini = float (input("Qual o valor do Salário minimo: "))

#Procedimento
valor_h_tb = (Salario_mini / 2)

valor_salario_bruto = valor_h_tb * Horas_trab

impostos = valor_salario_bruto * 3 / 100

Valor_salario_liquido = valor_salario_bruto - impostos

#Saida
print ("O sálario líquido será de: ",Valor_salario_liquido)