#19. Cada degrau de uma escada tem X de altura. Faça um programa que receba essa altura e a altura
#  que o usuário deseja alcançar subindo a escada, calcule e mostre quantos degraus ele deverá subir
#  para atingir seu objetivo, sem se preocupar com a altura do usuário. Todas as medidas fornecidas devem estar em metros.

 # LEIA altura_do_degrau
 # LEIA altura_desejada

 # quantidade_de_degraus = altura_desejada // altura_do_degrau

 # ESCREVA quantidade_degraus

 #Entrada
al_deg = int(input("Indique a altura do dregrau: "))

al_dej = int(input("Informe a altura desejada: "))

 #Prosedimento
quant_degraus = al_dej // al_deg

 #saida
print ("Qual a quantidade de degraus: ",quant_degraus)
