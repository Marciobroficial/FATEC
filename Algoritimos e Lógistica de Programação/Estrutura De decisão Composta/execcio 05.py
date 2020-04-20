############################################################################################
# 5. Elabore um algoritmo que informando a idade de um nadador o
# mesmo terá condições de classificar em uma das seguintes categorias:
#
# Categoria   Idade
# infantil     5 a 10 anos
# juvenil      11 a 17 anos
# adulto       maiores de 18 anos.
#############################################################################################
# Entrada
print ('<->'*35)
print()
idade = int (input('Qual a ideade do nadador: '))
if idade >= 5 and idade <= 10 :
  print ('Infantil')
elif idade >= 11 and idade <= 17:
  print ('Juvenil')
else:
  print('Adulto')
print ()
print ('<->'*35)  
##############################################################################################