# 23. Faça um programa para resolver equações do 2 o grau.

# ax² + bx + c = 0

# A variável a deve ser diferente de zero*

# delta = b ** 2 - 4 * a * c
# delta < 0. Não existe raiz real
# delta = 0. Existe uma raiz real
# x = (-b) / (2 * a)
# delta > 0. Existem duas raízes reais
# x1 = (-b + delta )/ (2 * a)
# x2 = (-b - delta )/ (2 * a)

# LEIA a, b, c

# SE a = 0
#     ESCREVA “Estes valores não formam uma equação de segundo grau” 
# SENÃO
#     delta = (b * b) – ( 4 * a * c)
#     SE delta < 0
#         ENTÃO ESCREVA “Não existe raiz real”
#     SE delta = 0
#         ESCREVA “Existe uma raiz real”
#         x1 = (– b) / (2 * a)
#         ESCREVA x1
#     SE delta > 0
#         ESCREVA “Existem duas raízes reais”
#         x1 = (– b) + raiz(delta) / (2 * a)
#         x2 = (– b) - raiz(delta) / (2 * a)
#         ESCREVA(x1, x2)
############################################################################################