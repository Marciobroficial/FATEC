########################################################################
# 2.Faça um algoritmo que leia o nome e a idade de uma pessoas,
# verifique se a idade de uma pessoa é menor ou maior de idade.
# Considera-se maior de idade uma pessoa com 18 anos ou mais.
# Como saída o algoritmo deve informar o nome e a idade da pessoa
# e depois uma mensagem se ela é ou não maior de idade.
#########################################################################
#Entrada de dados
print ('<->' * 25)
nome = input ("Digite seu nome: ")
idade = int (input("Diginte a sua idade: "))

#Procedimento
if idade >= 18:
 print ('Seu nome é:', (nome))
 print ('Sua idade é:', (idade))
 print ("Você é maior de idade", "")
else:
     print ("Você é menor de idade",)
print ('<->' * 25)