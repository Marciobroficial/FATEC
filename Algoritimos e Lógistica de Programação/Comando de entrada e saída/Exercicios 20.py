#20. Faça um programa que receba a medida do ângulo (em graus) formado por uma escada
#  apoiada no chão e encostada na parede e a altura da parede onde está a ponta da escada.
#  Calcule e mostre a medida dessa escada. Observação: as funções trigonométricas implementadas
#  nas linguagens de programação trabalham com medidas de ângulos em radianos.

# LEIA angulo
# LEIA altura

#  radiano = angulo * 3.14 / 180
#  escada = altura / seno(radiano)
#  ESCREVA escada

#entrada
import math 
angulo = float(input("informe a medida do ângulo: "))
altura =float(input("Qual é a altura da parede: "))

#Prosedimento
import math
radiano = angulo * 3.14 / 180
escada = altura  /math.sin(radiano)

print ("A escada tem como medida: ",escada)