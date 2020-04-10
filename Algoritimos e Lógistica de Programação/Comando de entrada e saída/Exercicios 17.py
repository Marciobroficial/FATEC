#17. Um trabalhador recebeu seu salário e o depositou em sua conta bancária. 
#Esse trabalhador emitiu dois cheques e agora deseja saber seu saldo atual. 
#O banco criou uma taxa para a operação bancária de retirada que tem que pagar um imposto, 
# chamado de cpmf, de 0.38% e o saldo inicial da conta está zerado.

#  LEIA salario
#  LEIA valor_cheque1
#  LEIA valor_cheque2

# cpmf_cheque1 = valor_cheque1 * 0.038 / 100
#  saque1 = valor_cheque1 + cpmf_cheque1
#  cpmf_cheque2 = cheque2 * 0.038 / 100
#  saque2 = valor_cheque2 + cpmf_cheque2
#  saldo = salario - saque1 - saque2

#  ESCREVA saldo

#Entrada
salario = float (input("Digite o Valor da Salário: "))

valor_cheque1 = float (input("Qual o valor do primeiro ch: "))

valor_cheque2 = float (input("Qual o valor o segundo ch: "))

#Procedimento
cpmf_cheque1 = valor_cheque1 * (0.038 / 100)

saque1 = valor_cheque1 + cpmf_cheque1

cpmf_cheque2 = valor_cheque2 * (0.038 / 100)

saque2 = valor_cheque2 + cpmf_cheque2

saldo = salario - saque1 - saque2

#Saida
print ("O saldo atual é: ",saldo)