#22. Sabe-se que o quilowatt de energia custa um quinto do salário mínimo.
#Faça um programa que receba o valor do salário mínimo e a quantidade
#de quilowatts consumida por uma residência. Calcule e mostre:

#o valor de cada quilowatt;
#o valor a ser pago por essa residência;
#o valor a ser pago com desconto de 15%.

#LEIA valor_do_salario
#LEIA quantidade_de_quilowatt

#valor_do_quilowatt = valor_do_salario / 5
#valor_em_reais ← valor_do_quilowatt * quantidade_de_quilowatt
#valor_do_desconto = valor_em_reais * 15 / 100
#valor_com_desconto =  valor_em_reais − valor_do_desconto

#ESCREVA valor_do_quilowatt
#ESCREVA valor_em_reais
#ESCREVA valor_com_desconto

#Entrada
salario = float (input("Digite o valor do salario minimo: "))
watt = float (input("QUal foi o consumo em Watts: "))

#procedimeto
valor_watt =  salario / 5
valor_didin = valor_watt * watt
valor_do_desc =  valor_didin * 15/100
valor_com_desc =  valor_didin - valor_do_desc

#Saída
print ("Qua o valor do quilowatt: ",valor_watt)
print ("Qual o valor gasto em reais: ",valor_didin)
print ("E qual o valor pago com desconto: ",valor_do_desc)