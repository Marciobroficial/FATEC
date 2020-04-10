#25. Faça um programa que receba o custo de um espetáculo teatral e o preço do convite desse espetáculo.
 #Esse programa deverá calcular e mostrar a quantidade de convites que devem ser vendidos para que, pelo menos,
 #o custo do espetáculo seja alcançado.

 # LEIA custo
 # LEIA convite

 # quantidade = custo / convite

 # ESCREVA quantidade

 # Entrada
custo = float (input("informe o valor do espetaculo: "))
convite = float (input("informe o valor do convite: "))

# Procedimento

quantidade = custo / convite

#Saida
print ("A quantidade de convite a ser vendida deve ser de: ",quantidade)