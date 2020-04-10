#18. Pedro comprou um saco de ração com peso em quilos. Ele possui dois gatos, 
# para os quais fornece a quantidade de ração em gramas. A quantidade diária de ração 
# fornecida para cada gato é sempre a mesma. Faça um programa que receba o peso do saco de ração 
# e a quantidade de ração fornecida para cada gato, calcule e mostre quanto restará de ração no saco após cinco dias.

#  LEIA peso_saco
#  LEIA racao_gato1
#  LEIA racao_gato2

#  Racao_gato1 = racao_gato1 / 1000
#  racao_gato2 = racao_gato2 / 1000
#  total_final = peso_saco − 5 * (racao_gato1 + racao_gato2)

#  ESCREVA total_final

#Entrada
peso_saco = float(input("Quanto pesa o saco: "))

r1 = float(input('Qual é a ração n1: '))

r2 = float(input('Qual a ração n2: '))

#Precedimento
r1 = r1 / 1000
r2 = r2 / 1000
resta_no_saco = peso_saco - 5 * (r1 + r2)

#saida
print ("A quantidade que resta no saco de ração e´: ",resta_no_saco)