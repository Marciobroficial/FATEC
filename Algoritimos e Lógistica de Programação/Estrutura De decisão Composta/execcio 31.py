# 31. Faça um programa que receba a medida de um ângulo em graus.
# Calcule e mostre o quadrante em que se localiza esse ângulo.
# Considere os quadrantes da trigonometria e, para ângulos
# maiores que 360° ou menores que −360o, reduzí-los, mostrando 
# também o número de voltas e o sentido da volta (horário ou anti-horário).

# SE angulo > 360 OU angulo < -360
#     voltas = parte inteira(angulo / 360)    
#     angulo = RESTO(angulo / 360)
# SENÃO 
#     voltas = 0
# SE angulo = 0 OU angulo = 90 OU angulo = 180
#            OU angulo = 270 OU angulo = 360
#            OU angulo = -90 OU angulo = -180
#            OU angulo = -270 OU angulo = -360
#   ESCREVA “Está em cima de algum dos eixos”
#   SE (angulo > 0 E angulo < 90) OU (angulo < -270 E angulo > -360)
#     ESCREVA “1o Quadrante”
#   SE (angulo > 90 E angulo < 180) OU (angulo < -180 E angulo > -270)
#     ESCREVA “2o Quadrante”
#   SE (angulo > 180 E angulo < 270) OU (angulo < -90 E angulo > -180)
#     ESCREVA “3o Quadrante”
#   SE (angulo > 270 E angulo < 360) OU (angulo < 0 E angulo > -90)
#     ESCREVA “4o Quadrante”
#   ESCREVA voltas, “ volta(s) no sentido “
# SE angulo < 0
#     ESCREVA “horário”
# SENÃO 
#     ESCREVA “anti-horário”
####################################################################################################################
