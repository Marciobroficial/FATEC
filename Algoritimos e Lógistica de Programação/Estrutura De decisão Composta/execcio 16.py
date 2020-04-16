##############################################################################################################
# 16. Faça um programa que determine a data cronologicamente maior entre duas datas fornecidas pelo usuário. 
# Cada data deve ser composta por três valores inteiros, em que o primeiro representa o dia,                 
# o segundo, o mês e o terceiro, o ano.                                                                      
#                                                                                                            
#  SE ano1 > ano2                                                                                            
#      ESCREVA “A maior data é: “,dia1,”-”,mes1,”-”,ano1                                                     
#  SENÃO SE ano2>ano1                                                                                        
#      ESCREVA “A maior data é: “,dia2,”-”,mes2,”-”,ano2                                                     
#  SENÃO SE mes1>mes2                                                                                        
#      ESCREVA “A maior data é: “,dia1,”-”,mes1,”-”,ano1
#  SENÃO SE mes2>mes1
#      ESCREVA “A maior data é: “,dia2, “-”,mes2,”-”,ano2
#  SENÃO SE dia1>dia2
#      ESCREVA “A maior data é: “-”,dia1,”-”,mia1,” -”,ano1
#  SENÃO SE dia2>dia1
#      ESCREVA “A maior data é: “,dia2,” -”,mes2,”-”,ano2
#  SENÃO
#      ESCREVA “As datas são iguais!”
################################################################################################################
print('<->' * 25)

print('\nPrimeiro Ano')
dia = int (input( 'Digite o Dia: '))
mes = int (input( 'Digite o mes: '))
ano = int (input( 'Digite o Ano: '))

print('<->' * 25)

print ('\nSegundo Ano')
dia2 = int (input( 'Digite o Dia: '))
mes2 = int (input( 'Digite o mes: '))
ano2 = int (input( 'Digite o Ano: '))

print('<->' * 25)

print(ano == ano2)
if  ano  >  ano2 :
    print ( 'A maior data é: {} / {} / {}' .format ( dia , mes , ano ))
elif ano2  >  ano :
    print ( 'A maior data é: {} / {} / {}' .format ( dia2 , mes2 , ano2 ))
elif mes  >  mes2 :
    print ( 'A maior data é: {} / {} / {}' .format ( dia , mes , ano ))
elif mes2  >  mes :
    print ( 'A maior data é: {} / {} / {}' .format ( dia2 , mes2 , ano2 ))
elif dia >  dia2 :
    print ( 'A maior data é: {} / {} / {}' .format ( dia , mes , ano ))
elif dia2  >  dia :
    print ( 'A maior data é: {} / {} / {}' .format ( dia2 , mes2 , ano2 ))
else :
    print ( '\nAs datas são iguais!\n' )
    print ('<->' *25)    
      
