#################################################################################################################################################
# Faça um algoritmo que calcule e exiba o salário reajustado
# de um funcionário de acordo com a seguinte regra:
# Salário até 300, reajuste de 50%;
# Salários maiores que 300, reajuste de 30%.
##################################################################################################################################################
#Entrada de dados
print ('<->' *25) # linha de separação
salario = float (input("Digite o Salário Atual: R$ ")) # indica o salario da pessoa
print ('<->' *25) # linha de separação
#Processamento
if salario <= 300: 
   bonus = salario * 50/100     
   nv = salario + bonus  # nv = novo slario
   print ('Salario atual é: R$',salario, '\nCom reajuste de 50%: R$',bonus,'\nSalário final: R$',nv) # formato 01 de se fazer
elif salario > 300 :
    bonus = salario * 30/100
    nv = salario + bonus
    print ('Salario atual é: R$: {:.2f} \nCom reajuste de 30%: R$ {:.2f} \nSalário final: R$: {:.2f}'.format (salario , bonus , nv )) # formato 02 de fazer

