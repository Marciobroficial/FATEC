#####################################################################################################################
# Faça um algoritmo que calcule e exiba o salário reajustado
# de um funcionário de acordo com a seguinte regra:
# Salário até 300, reajuste de 50%;
# Salários maiores que 300, reajuste de 30%.
#####################################################################################################################

print ('<->' *35)
salario = float (input("\nDigite o Salário Atual: R$ "))
if salario <= 300: 
   bonus = salario * 50/100     
   nv = salario + bonus 
   print ('\nSalario atual é: R$: ',salario, '\nCom reajuste de 50%: R$ ',bonus,'\nSalário final: R$: ',nv)
elif salario > 300 :
    bonus = salario * 30/100
    nv = salario + bonus
    print ('\nSalario atual é: R$: {:.2f} \nCom reajuste de 30%: R$ {:.2f} \nSalário final: R$: {:.2f}'.format (salario , bonus , nv ))
print()
print ('<->'* 35)

