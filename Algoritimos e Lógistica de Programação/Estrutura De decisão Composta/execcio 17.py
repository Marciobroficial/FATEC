##########################################################################################################################
# 17. Faça um programa que receba a hora do início de um jogo e a hora do término (cada hora é composta por duas variáveis inteiras: hora e minuto). Calcule e mostre a duração do jogo (horas e minutos),
# sabendo que o tempo máximo de duração do jogo é de 24 horas e que ele pode começar em um dia e terminar no dia seguinte.
#
# SE min_inicial > min_f
#   minuto_final = minuto_final + 60
#    hora_final = hora_final – 1
# SE hora_inicial > hora_final
#   hora_final = hora_final + 24
# minuto_duracao = minuto_final - minuto_inicial
# hora_duracao = hora_final - hora_inicial
###########################################################################################################################
print ('<->' * 35)
hora_inic  =  int ( input ( '\nDigite a hora em que o jogo começa :- ' ))
minuto_inic =  int ( input ( 'Agora digite os minutos :- ' ))
hora_final  =  int ( input ( 'Digite a hora em que o jogo termina :- ' ))
minuto_final =  int ( input ( 'Digite os minutos finais :- ' ))

if  minuto_inic  >  minuto_final :
      minuto_final  =  minuto_final  +  60
      hora_final  =  hora_final  - 1
if  hora_inic  >  hora_final :
      hora_final  =  hora_final  +  24
minuto_duração  =  minuto_final  -  minuto_inic
hora_duração  =  hora_final  -  hora_inic
print ('O jogo durou {} horas: {} minutos\n' .format ( hora_duração , minuto_duração ))
print ('<->' * 35)

