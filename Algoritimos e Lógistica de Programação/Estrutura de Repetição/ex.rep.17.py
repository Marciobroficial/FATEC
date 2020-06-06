17. Faça um programa que leia o número de termos, determine e mostre os valores de acordo com a série a seguir:
Série = 2, 7, 3, 4, 21, 12, 8, 63, 48, 16, 189, 192, 32, 567, 768...

ALGORITMO
LEIA numero_de_termos
 
termo1 = 2
termo2 = 7
termo3 = 3
 
termo_atual = 4
 
ENQUANTO termo_atual <= numero_de_termos
    ESCREVA termo1, termo2, termo3
 
    termo1 = termo1 * 2
    ESCREVA termo1
    termo_atual += 1
 
    SE termo_atual <= numero_de_termos
        termo2 = termo2 * 3
        ESCREVA termo2
        termo_atual += 1
 
    SE termo_atual <= num_termos
        termo3 = termo3 * 4
        ESCREVA termo3
        termo_atual += 1