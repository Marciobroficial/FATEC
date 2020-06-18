# 16. Faça um programa que monte os oito primeiros termos da sequência de Fibonacci.
# ALGORITMO
# numero_de_elementos_da_sequencia = 8
# elementoN = 0
# elementoNmais1 = 1
 
# ESCREVA elementoN
# ESCREVA elementoNmais1
 
# PARA elemento NO INTERVALO DE 3 ATÉ numero_de_elementos_da_sequencia
#     valor_do_fibonacci_atual = elementoN + elementoNmais1
 
#     ESCREVA valor_do_fibonacci_atual
 
#     elementoN = elementoNmais1
#     elementoNmais1 = valor_do_fibonacci_atual
#-------------------------------------------------------------------------------------------#

nElementos = 8
elementoN = 0
elementoNmais1 = 1
print("A sucessão de Fibonacci começa normalmente por {} e {} "
      "e cada termo subsequente corresponde à soma dos dois anteriores.".format(elementoN, elementoNmais1))

print("Os próximos 8 elementos da sequencia Fibonacci são:")
for c in range(nElementos):
    vFibonacciAtual = elementoN + elementoNmais1
    print(vFibonacciAtual)
    elementoN = elementoNmais1
    elementoNmais1 = vFibonacciAtual