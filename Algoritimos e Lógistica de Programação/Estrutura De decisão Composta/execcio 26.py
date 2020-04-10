26. Faça um programa que receba:
O código de um produto comprado, supondo que a digitação do código do produto seja sempre válida, isto é, um número * inteiro entre 1 e 10.
O peso do produto em quilos.
O código do país de origem, supondo que a digitação do código seja sempre válida, isto é, um número inteiro entre 1 e 3.
CÓDIGO DO PAÍS DE ORIGEM	IMPOSTO
1	0%
2	15%
3	25%
CÓDIGO DO PAÍS DO PRODUTO	IMPOSTO
1 a 4	10
5 a 7	25
8 a 10	35
Calcule e mostre:

o peso do produto convertido em gramas;
o preço total do produto comprado;
valor do imposto, sabendo que ele é cobrado sobre o * preço total do produto comprado e dependendo país de origem;
o valor total, preço total do produto mais imposto.
LEIA codigo_do_produto, peso_quilos, codigo_do_paiz
peso_em_gramas = peso_quilos * 1000
ESCREVA peso_em_gramas
SE codigo_do_produto >= 1 E codigo_do_produto <= 4
   preco_por_grama = 10
SE codigo_do_produto >= 5 E codigo_do_produto <= 7
   preco_por_grama = 25
SE codigo_do_produto >= 8 E codigo_do_produto <= 10
   preco_por_grama = 35    
preco_total = peso_em_gramas *preco_por_grama
ESCREVA preco_total
SE codigo_do_paiz = 1
    imposto = 0
SE codigo_do_paiz = 2
    imposto = preco_total * 15/100
SE codigo_do_paiz = 3
    imposto = preco_total * 25/100    
ESCREVA imposto
valor_total = preco_total + imposto
ESCREVA valor_total