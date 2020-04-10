# 3. Tendo como dados de entrada a altura e o sexo (M/F)
# de uma pessoa (M-masculino ou F-feminino),
# construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:

# homem: (72.7 * altura) - 58;

# mulher: (62.1 * altura) - 44.7

#entrada
altura = float (input ('Digite a sua altura: '))
sexo = input ('Digite seu sexo M ou F: ')

#Procedimento
h = (72.7*altura) - 58
m = (62.1*altura) - 44
if sexo == 'M' or sexo == 'm':
  print ('Masculino')
  print ('Seu peso Ideal',h)
elif sexo == 'F' or sexo == 'f':
  print ('Feminino')
  print ('Peso Ideal',m)
else:
    print ('Sexo Invalido')