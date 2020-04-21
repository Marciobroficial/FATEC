##########################################################################################################################
# 7. A Organização Mundial de Saúde usa a seguinte tabela para determinar a condição de um adulto,
# para isso desenvolva um algoritmo para calcular o Índice de Massa Corporal (IMC) e apresenta-lo, dado pela fórmula:
#
# IMC = peso / (altura)2   (o 2 elevado ao quadrado)
#
#  CONDIÇÃO	IMC         Em adultos
#  Abaixo do peso	    Abaixo de 18.5
#  No peso normal	    Entre 18.5 e 25
#  Acima do peso	    Entre 25.1 e 30
#  Obeso	            Acima de 30
############################################################################################################################
print('<->'*35)
print()
peso = float (input('Qual seu peso: '))
alt = float (input ('Qual sual altura: '))
imc = peso / (alt**2)
print ('Imc',imc)
if imc <= 18.5 :
    print ('vc está abixo do peso')
elif imc >= 18.5 and imc<= 25:
    print ('Você está no peso ídeal')
elif imc >= 25.1 and imc <= 30:
    print ('Você está Acima do peso')
else:
     print ('Você está Obeso')
print()
print('<->'*35)     
##     