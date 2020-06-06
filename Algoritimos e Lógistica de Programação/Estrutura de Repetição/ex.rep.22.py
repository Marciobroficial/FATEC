22. Faça um programa que receba:
o preço unitário,
a refrigeração (S para os produtos que necessitem de refrigeração e N para os que não necessitem)
a categoria (A — alimentação; L — limpeza; e V — vestuário)
Calcule e mostre:

O custo de estocagem, calculado de acordo com a tabela a seguir.
Preço unitário	Refrigeração	Categoria	Custo de estocagem
Até 20	-	A	2,00
Até 20	-	L	3,00
Até 20	-	V	4,00
----------------------	----------------------	----------------------	----------------------
Entre 20 e 50 (inclusive)	S	-	6,00
Entre 20 e 50 (inclusive)	N	-	0,00
----------------------	----------------------	----------------------	----------------------
Maior que 50	S	A	5,00
Maior que 50	S	L	2,00
Maior que 50	S	V	4,00
Maior que 50	N	A ou V	0,00
Maior que 50	N	L	1,00
O imposto calculado de acordo com as regras a seguir:
Se o produto possuir categoria A e refrigeração S, seu imposto será de 2% sobre o preço unitário; caso contrário, será de 4%.
O preço final, ou seja, preço unitário mais custo de estocagem mais imposto.
A classificação calculada usando a tabela a seguir.
Preço final	Classificação
Até 20,00	Barato
Entre 20,00 e 100,00 (inclusive)	Normal
Acima de R$ 100,00	Caro
A média dos valores adicionais, ou seja, a média dos custos de estocagem e dos impostos dos doze produtos.
O maior preço final.
O menor preço final.
O total dos impostos.
A quantidade de produtos com classificação barato.
A quantidade de produtos com classificação caro.
A quantidade de produtos com classificação normal.
ALGORITMO
total_de_produtos = 12
 
total_de_produtos_baratos = 0
total_de_produtos_normais = 0
total_de_produtos_caros = 0
 
total_de_custos_adicionais = 0
 
PARA produto NO INTERVALO DE total_de_produtos
    LEIA preco_do_produto, produto_necessita_de_refrigeracao, categoria_do_produto
 
    SE preco_do_produto <= 20
        SE categoria_do_produto == "A"
            custo_de_estocagem = 2
        SE categoria_do_produto == "L"
            custo_de_estocagem = 3
        SE categoria_do_produto == "V"
            custo_de_estocagem = 4
 
    SE  prodo_do_produto > 20 E preco_do_produto <= 50
        SE produdo_necessida_de_refrigeracao == "S"
            custo_de_estocagem = 6
        SENAO
            custo_de_estocagem = 0
 
    SE preco_do_produto > 50
        SE produdo_necessida_de_refrigeracao == "S"
            SE categoria_do_produto == "A"
                custo_de_estocagem = 5
            SE categoria_do_produto == "L"
                custo_de_estocagem = 2
            SE categoria_do_produto == "V"
                custo_de_estocagem = 4
        SENAO
            SE categoria_do_produto = "A" OU categoria_do_produto = "V"
                custo_de_estocagem = 0
            SE cagegoria_do_produto = "L"
                custo_de_estocagem = 1
 
    SE categoria_sobre_o_produto == "A" e produdo_necessida_de_refrigeracao == "S"
        imposto_do_produto = 2 / 100
    SENAO
        imposto_sobre_o_produto = 4 / 100
 
    preco_final_sobre_produto = preco_do_produto + custo_de_estocagem_do_produto + imposto_sobre_o_produto
 
  ESCREVA custo_de_estocagem_do_produto, imposto_sobre_o_produto, preco_final_do_produto
 
  SE preco_final_sobre_produto <= 20
      total_de_produtos_baratos += 1
      classificacao_do_produto = "PRODUTO BARATO"
 
  SE preco_final_sobre_produto >  20 E preco_final_sobre_produto <=  20
      total_de_produtos_normais += 1
      classificacao_do_produto = "PRODUTO NORMAL"
 
  SE preco_final_sobre_produto >  100
      total_de_produtos_caros += 1
      classificacao_do_produto = "PRODUTO CARO"
 
  custo_adicional_do_produto = custo_de_estocagem_do_produto + imposto_sobre_o_produto
 
   total_de_custo_adicionais_de_todos_produtos += custo_adicional_do_produto
   total_de_impostos_de_todos_os_produtos += imposto_sobre_o_produto
 
   SE produto == 0
      preco_do_produto_mais_caro = preco_final_do_produto
      preco_do_produto_mais_barato = preco_final_do_produto
   SENAO
      SE preco_do_produto_mais_caro < preco_final_do_produto
          preco_do_produto_mais_caro = preco_final_do_produto
      SE preco_do_produto_mais_barato > preco_final_do_produto
          preco_do_produto_mais_barato = preco_final_do_produto
 
media_dos_valores_adicionais = total_de_custo_adicionaisl_de_todos_produtos / total_de_produtos
 
ESCREVA media_dos_valores_adicionais
ESCREVA preco_do_produto_mais_caro
ESCREVA preco_do_produto_mais_barato
ESCREVA total_de_produtos_baratos
ESCREVA total_de_produtos_normais
ESCREVA total_de_produtos_caros