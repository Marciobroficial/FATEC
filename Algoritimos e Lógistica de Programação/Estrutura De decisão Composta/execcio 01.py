# Faça um algoritmo que calcule e exiba o salário reajustado
# de um funcionário de acordo com a seguinte regra:
# Salário até 300, reajuste de 50%;
# Salários maiores que 300, reajuste de 30%.

#Entrada de dados
salario = float (input("Digite o Salário Atual: "))
#Processamento
if salario <= 300:
   bonus = salario * 50/100     
   nv = salario + bonus  # nv = novo slario
   print ("Salario atual é: R$",salario, "Mais 50%, de reajuste R$",bonus,"Salário final: R$",nv)
else:
    bonus = salario * 30/100
    nv = salario + bonus
    print ("Salario atual é: R$",salario, "Mais 30%, de reajuste R$",bonus,"Salário final: R$",nv)
