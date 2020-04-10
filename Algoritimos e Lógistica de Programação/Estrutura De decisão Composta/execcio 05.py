# 5. Elabore um algoritmo que informando a idade de um nadador o
# mesmo terá condições de classificar em uma das seguintes categorias:

# infantil = 5 - 10 anos;

# juvenil = 11-17 anos;

# adulto = maiores de 18 anos.

# Entrada
idade = int (input('Qual a ideade do nadador: '))
if idade >= 5 and idade <= 10 :
  print ('Infantil')
elif idade >= 11 and idade <= 17:
  print ('Juvenil')
else:
  print('Adulto')
