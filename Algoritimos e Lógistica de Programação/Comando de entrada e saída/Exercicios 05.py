#Entrada de dados

salario = float (input('qual o salário?: ' ))
percentual = float (input('E qual o percentual para o aumento: '))

#Processamento

aumento = salario * (percentual / 100)
soma = salario + aumento


#Saida de dados

print ('O novo salário será de: ',soma)