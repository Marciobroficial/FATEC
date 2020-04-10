#Entrada de dados

salbase = float (input('Qual é o Salário Base do Funcionário: '))


#Processamento

gratificacao = salbase * (5 / 100)
imposto = salbase * (7 / 100)
salario_a_receber = salbase + gratificacao - imposto


#Saida de dados
print ('Salario a Receber: ',salario_a_receber)