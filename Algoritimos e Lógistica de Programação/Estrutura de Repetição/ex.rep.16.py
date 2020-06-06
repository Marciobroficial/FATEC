16. Faça um programa que monte os oito primeiros termos da sequência de Fibonacci.
ALGORITMO
numero_de_elementos_da_sequencia = 8
elementoN = 0
elementoNmais1 = 1
 
ESCREVA elementoN
ESCREVA elementoNmais1
 
PARA elemento NO INTERVALO DE 3 ATÉ numero_de_elementos_da_sequencia
    valor_do_fibonacci_atual = elementoN + elementoNmais1
 
    ESCREVA valor_do_fibonacci_atual
 
    elementoN = elementoNmais1
    elementoNmais1 = valor_do_fibonacci_atual