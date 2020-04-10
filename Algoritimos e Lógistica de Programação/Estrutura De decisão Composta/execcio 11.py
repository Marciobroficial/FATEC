#11. Faça um programa que receba três números e mostre-os em ordem crescente.
# Suponha que o usuário digitará três números diferentes.

# SE numero1 < numero2 E numero1 < numero3
#    SE numero2 < numero3
#        ESCREVA “A ordem crescente é: “,numero1,“-”,numero2,“-”,numero3
#    SENÃO
#        ESCREVA “A ordem crescente é: “,numero1,“-”,num3,“-”,num2
# SE numero2 < numero1 E numero2 < numero3
#    SE numero1 < numero3
#        ESCREVA “A ordem crescente é: “,numero2,“-”,numero1,“-”,numero3
#    SENÃO
#        ESCREVA “A ordem crescente é: “,numero2,“-”,numero3,“-”,numero
# SE numero3 < numero1 E numero3 < num2
#   SE numero1 < numero2
#      ESCREVA “A ordem crescente é: “,numero3,“-”,numero1,“-”,numero2

n1 = float (input ('Digite o 1º numero: '))
n2 = float (input ('Digite o 2º numero: '))
n3 = float (input ('Digite o 3º numero: '))

if n1 < n2 and n1 < n3: # verifica se o primeiro número é maior que o segundo e o terceiro
    if n2 < n3: # verifica se o segundo número é maior que o terceiro
        print('A ordem crescente é: {:.0f} - {:.0f} - {:.0f}'.format(n1, n2, n3))
    else:
        print('A ordem crescente é: {:.0f} - {:.0f} - {:.0f}'.format(n1, n3, n2))
if n2 < n1 and n2 < n3: # verifica se o segundo número é maior que o primeiro e o terceiro
    if n1 < n3:  # verifica se o primeiro número é maior que o terceiro
        print('A ordem crescente é: {:.0f} - {:.0f} - {:.0f}'.format(n2, n1, n3))
    else:
        print('A ordem crescente é: {:.0f} - {:.0f} - {:.0f}'.format(n2, n3, n1))
if n3 < n1 and n3 < n2: # verifica se o último número é maior que o primeiro e o segundo
    if n1 < n2: # verifica se o último número é maior que o primeiro e o segundo
        print('A ordem crescente é: {:.0f} - {:.0f} - {:.0f}'.format(n3, n1, n2))
    else:
        print('A ordem crescente é:: {:.0f} - {:.0f} - {:.0f}'.format(n3, n2, n1))