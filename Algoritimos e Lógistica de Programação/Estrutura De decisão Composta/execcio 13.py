#13. Faça um programa que receba quatro valores: I, A, B e C.
# Desses valores, I é inteiro e positivo, A, B e C são reais. Escreva os números A, B e C obedecendo à tabela a seguir.
# Suponha que o valor digitado para I seja sempre um valor válido, ou seja, 1, 2 ou 3,.
# E que os números digitados sejam diferentes um do outro.

# VALOR DE I	    FORMA A ESCREVER
#
# 1	A, B e C ------ em ordem crescente.
# 2	A, B e C ------ em ordem decrescente
# 3	--------------- O maior fica entre os outros dois números.

# SE I == 1
#    SE A<B E A<C
#        SE B<C
#            ESCREVA “A ordem crescente dos números é:”,A,” -”,B,”-”,C
#        SENÃO
#            ESCREVA “A ordem crescente dos números é:”,A,” -”,C,”-”,B
#    SE B<A E B<C
#        SE A<C
#            ESCREVA “A ordem crescente dos números é:”,B,”-”,A,”-”,C
#        SENÃO
#            ESCREVA “A ordem crescente dos números é: “,B,”-”,C,”-”,A
#    SE C<A E C<B
#        SE A<B
#            ESCREVA “A ordem crescente dos números é: “,C,”-”,A,”-”,B
#        SENÃO
#            ESCREVA “A ordem crescente dos números é: “,C,”-”,B,”-”,A
# SE I == 2
#   SE A>B E A>C
#        SE B>C
#            ESCREVA “A ordem decrescente dos números é: “,A,” -”,B,”-”,C
#        SENÃO
#            ESCREVA “A ordem decrescente dos números é: “,A,” -”,C,”-”,B
#    SE B>A E B>C
#        SE A>C
#            ESCREVA “A ordem decrescente dos números é: “,B,” -”,A,”-”,C
#        SENÃO
#            ESCREVA “A ordem decrescente dos números é: “,B,” -”,C,”-”,A
#    SE C>A E C>B
#        SE A>B
#            ESCREVA “A ordem decrescente dos números é: “,C,” -”,A,”-”,B
#        SENÃO
#            ESCREVA “A ordem decrescente dos números é: “,C,” -”,B,”-”,A
# SE I == 3
#    SE A>B E A>C
#        ESCREVA “A ordem desejada é: “,B,”-”,A,”-”,C
#    SE B>A E B>C
#        ESCREVA “A ordem desejada é: “,A,”-”,B,”-”,C
#    SE C>A E C>B
#        ESCREVA “A ordem desejada é: “,A,”-”,C,”-”,B
#
#######################################################################################################################
#
#   1 A, B e C em ordem crescente.
#   2 A, B e C em ordem decrescente
#   3 O maior fica entre os outros dois números.
#
#######################################################################################################################
print ('<->' *25)
A = int (input('\nDigite um valor para A: '))
B = int (input ('Digite um valor para B: '))
C = int (input ('Digite um valor para C: '))
print ('<->' *25)
I = int ( input ('\n(1) ordem crescente \n(2) ordem decrescente \n(3) número maior ao centro \nSelecione uma das opções acima:-> '))
print ('<->' *25)
if I == 1:
    if A<B and A<C:
        if B<C:
            print ('\nA ordem crescente dos números é: {} - {} - {}\n' .format ( A, B, C ))
            print ('<->' *25)
        else:
            print ('\nA ordem crescente dos números é: {} - {} - {}\n' .format ( A, C, B ))
            print ('<->' *25)
    if B<A and B<C:
        if A<C:
            print ( '\nA ordem crescente dos números é: {} - {} - {}\n' .format ( B, A, C ))
            print ('<->' *25)
        else:
            print ( '\nA ordem crescente dos números é: {} - {} - {}\n' .format ( B, C, A ))
            print ('<->' *25)
    if C<A and C<B:
        if A<B:
            print ( '\nA ordem crescente dos números é:  {} - {} - {}\n' .format ( C, A, B ))
            print ('<->' *25)
        else:
            print ( '\nA ordem crescente dos números é:  {} - {} - {}\n' .format ( C, B, A ))
            print ('<->' *25)
if  I  ==  2 :
    if  A  >  B  and  A  >  C :
        if  B  >  C :
            print ( '\nA ordem decrescente dos números digitados é: {} - {} - {}\n' .format ( A , B , C ))
            print ('<->' *25)
        else:
            print ( '\nA ordem decrescente dos números digitados é: {} - {} - {}\n' .format ( A , C , B ))
            print ('<->' *25)
    if  B  >  A  and  B  >  C :
        if  A  >  C :
            print ( '\nA ordem decrescente dos números digitados é: {} - {} - {}\n' .format ( B , A , C ))
            print ('<->' *25)
        else:
            print ( '\nA ordem decrescente dos números digitados é: {} - {} - {}\n' .format ( B , C , A ))
            print ('<->' *25)
    if  C  >  A  and  C  >  B :
        if  A  >  B :
            print ( '\nA ordem decrescente dos números digitados é: {} - {} - {}\n' .format ( A , B , C ))
            print ('<->' *25)
        else:
            print ( '\nA ordem decrescente dos números digitados é: {} - {} - {}\n' .format ( A , C , B ))
            print ('<->' *25)
if  I  ==  3 :
    if  A  >  B  and  A  >  C :
        print ( '\nO pedido solicitado é: {} - {} - {}\n' .format ( B , A , C ))
        print ('<->' *25)
    if  B  >  A  and  B  >  C :
        print ( '\nO pedido solicitado é: {} - {} - {}\n' .format ( A , B , C ))
        print ('<->' *25)
    if  C  >  A  and  C  >  B :
        print ( '\nO pedido solicitado é: {} - {} - {}\n' .format ( A , C , B ))
        print ('<->' *25)
if I > 3:
        print ('\nA opção escolhida não existe\n')
        print ('<->' *25)                   