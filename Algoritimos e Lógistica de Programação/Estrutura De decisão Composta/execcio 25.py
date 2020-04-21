# 25. Faça um programa que receba a altura e peso de uma pessoa.
# De acordo com a tabela a seguir, verifique e mostre a classificação dessa pessoa.

#   ALTURA	            ATÉ 60	    ENTRE 60 E 90 (INCLUSIVE)	        ACIMA DE 90
#   Menores que 1,20	    A	        D	                                G
#   De 1,20 a 1,70  	    B	        E	                                H
#   Maiores que 1,70	    C	        F	                                I

# LEIA altura, peso
# SE altura < 1.20
#    SE peso <= 60
#        ENTÃO ESCREVA “A”
#    SE peso > 60 E peso <= 90
#        ENTÃO ESCREVA “D”
#    SE peso > 90
#        ENTÃO ESCREVA “G”
# SE altura >= 1.20 E altura <= 1.70
#    SE peso <= 60
#        ESCREVA “B”
#    SE peso > 60 E peso <= 90
#        ESCREVA “E”
#    SE peso > 90
#        ESCREVA “H”
# SE altura > 1.70
#    SE peso <= 60
#        ESCREVA “C”
#    SE peso > 60 E peso <= 90
#        EESCREVA “F”
#    SE peso > 90
#        ESCREVA “I”
################################################################################################################
print ('<->' *35)
# armazena informações inseridas pelo usuário
altura = float ( input ( '\nInsira a altura da pessoa aqui no seguinte formato: (M.CM) :> ' ))
peso = float ( input ( 'Insira o peso da pessoa aqui no seguinte formato: (K.GM) :> ' ))
if altura < 1.20:
    if peso <= 60:
        print ( '\nVocê está na categoria A\n' )
    elif peso > 60 and peso <=  90:
        print ( '\nVocê está na categoria D\n' )
    elif peso > 90 :
        print ( '\nVocê está na categoria G\n' )
elif  altura  >= 1.2 and altura <= 1.7:
    if  peso  <= 60:
        print ( '\nVocê está na categoria B\n' )
    elif peso > 60 and peso <= 90:
        print ( '\nVocê está na categoria E\n' )
    elif peso > 90:
        print ( '\nVocê está na categoria H\n' )
elif altura > 1.7:
    if  peso  <= 60:
        print ( '\nVocê está na categoria C\n' )
    elif peso > 60 and peso <= 90:
        print ( '\nVocê está na categoria F\n' )
    elif peso > 90:
        print ( '\nVocê está na categoria I\n' )
print ('<->' *35)