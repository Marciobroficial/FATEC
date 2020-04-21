#####################################################################################################################
# 15. Faça um programa que mostre a data e a hora do sistema 
# os seguintes formatos: DD/MM/AAAA – mês por extenso e hora:minuto.
# Observação: from carrega um módulo/biblioteca da linguagem Python
# e o import é usado para informar qual objeto desta biblioteca queremos importar
#
#   from datetime import datetime
#   hoje = datetime.now()
#   print (hoje.year)
#   print (hoje.month)
#   print (hoje.day)
#   print (hoje.hour)
#   print (hoje.minute)
#   print (hoje.second)
#
#####################################################################################################################
from  datetime  import  datetime 
print ('<->' *44)
hoje = datetime . now () 
if  hoje . month  ==  1 :
    month  = ( 'janeiro' )
    hour =  hoje . hour  -  3
elif  hoje . month  ==  2 :
    month  = ( 'fevereiro' )
    hour =  hoje . hour  -  3
elif  hoje . month  ==  3 :
    month  = ( 'março' )
    hour =  hoje . hour  -  3
elif  hoje . month  ==  4 :
    month  = ( 'abril' )
    hour =  hoje . hour  -  3
elif  hoje . month  ==  5 :
    month  = ( 'maio' )
    hour =  hoje . hour  -  3
elif  hoje . month  ==  6 :
    month  = ( 'junho' )
    hour =  hoje . hour  -  3
elif  hoje . month  ==  7 :
    month  = ( 'julho' )
    hour =  hoje . hour  -  3
elif  hoje . month  ==  8 :
    month  = ( 'agosto' )
    hour =  hoje . hour  -  3
elif  hoje . month  ==  9 :
    month  = ( 'setembro' )
    hour =  hoje . hour  -  3
elif  hoje . month  ==  10 :
    month  = ( 'outubro' )
    hour =  hoje . hour  -  3
elif  hoje . month  ==  11 :
    month  = ( 'novembro' )
    hour =  hoje . hour  -  3
elif  hoje . month  ==  12 :
    month  = ( 'dezembro' )
    hour =  hoje . hour  -  3
print ( '\nA data e a hora atual é: {:02d} / {} / {} - {:02d}:{:02d}:{:02d} \n'.format ( hoje . day , month , hoje . year , hoje . hour , hoje . minute , hoje . second ))
print ('<->' *44)
##