###########################################################################################################################
# 8. A nota final de um estudante é calculada a partir de três notas atribuídas,
# respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final.
# A média das três notas mencionadas obedece aos pesos a seguir:
#
#   NOTA	                    PESO
#   Trabalho de laboratório	    2
#   Avaliação semestral	        3
#   Exame final	                5
#
# Faça um programa que receba as três notas, calcule e mostre a média ponderada e o conceito que segue a tabela
#
#   MÉDIA PONDERADA	        CONCEITO
#   8,0 <= média <= 10	    A
#   7,0 <= média < 8,0	    B
#   6,0 <= média < 7,0	    C
#   5,0 <= média < 6,0	    D
#   0,0 <= média < 5,0	    E
#
# media_ponderada = (nota_traballho * 2 + avaliacao_semestral * 3 + exame_final * 5) / 10
###########################################################################################################################
print('<->'*35)
print()
m1 = float (input ('Nota Trabalho de Laboratorio: '))
m2 = float (input ('Nota Avaliação Semestral: '))
m3 = float (input ('Nota Exame Final: '))
mp = (m1*2 + m2*3 + m3*5) /10
print ('A média é: ',mp)
if mp >= 8.0 and mp <= 10:
    print ('conceito A')
elif mp > 7.0 and mp < 8.0:
    print ('conceito B')
elif mp >6.0 and mp < 7.0:
    print ('conceito C')
elif mp > 5.0 and mp < 6.0:
    print ('conceito D')
else:
    print ('conceito E')
print()
print('<->'*35)     
##