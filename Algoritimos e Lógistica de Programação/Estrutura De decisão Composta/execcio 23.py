#########################################################################################################################
# 23. Faça um programa para resolver equações do 2 o grau.
#
#       ax² + bx + c = 0
#
#   A variável a deve ser diferente de zero*
#
#   delta = b ** 2 - 4 * a * c
#   delta < 0. Não existe raiz real
#   delta = 0. Existe uma raiz real
#   x = (-b) / (2 * a)
#   delta > 0. Existem duas raízes reais
#   x1 = (-b + delta )/ (2 * a)
#   x2 = (-b - delta )/ (2 * a)
#
#   LEIA a, b, c
#
#   SE a = 0
#        ESCREVA “Estes valores não formam uma equação de segundo grau” 
#   SENÃO
#       delta = (b * b) – ( 4 * a * c)
#        SE delta < 0
#           ENTÃO ESCREVA “Não existe raiz real”
#        SE delta = 0
#          ESCREVA “Existe uma raiz real”
#             x1 = (– b) / (2 * a)
#             ESCREVA x1
#        SE delta > 0
#             ESCREVA “Existem duas raízes reais”
#             x1 = (– b) + raiz(delta) / (2 * a)
#             x2 = (– b) - raiz(delta) / (2 * a)
#             ESCREVA(x1, x2)
############################################################################################
print ('<->' *35)
a = int (input('\n De um numero real para < a >: '))
if a == 0:
    print (' Estes valores não formam uma equação de segundo grau')
else:   
    b = int (input(' De um numero real para < b >: '))
    c = int (input(' De um numero real para < c >: '))
    delta = (b * b) - ( 4* a * c)
    if delta < 0:
        print ('\n Não existe raiz real\n') 
    elif delta == 0:
         print ('existe uma raiz ral!')
         x1 = (-b) / (2 * a)
    elif delta > 0:
        print ('\nExistem duas raízes real!')
        x1 = (-b + delta) / (2 * a)    
        x2 = (-b - delta) / (2 * a)
        print ('As raises rais são: {: .2f} e {: .2f} \n' .format (x1 , x2))
print ('<->' *35)