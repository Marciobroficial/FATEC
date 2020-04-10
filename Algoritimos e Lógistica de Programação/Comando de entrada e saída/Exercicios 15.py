# O custo ao consumidor de um carro novo é a soma do preço de fábrica com o percentual
# e lucro do distribuidor e dos impostos aplicados ao preço de fábrica. Faça um programa que receba o preço de fábrica de um veículo, 
# o percentual de lucro do distribuidor e o percentual de impostos, calcule e mostre:
#o valor correspondente ao lucro do distribuidor;
#o valor correspondente aos impostos;
#o preço final do veículo.

#  LEIA preco_de_fabrica
#  LEIA percentual_de_lucro_do_distribuidor
#  LEIA percentual_do_imposto
#  lucro_do_distribuidor = preco_de_fabrica * percentual_de_lucro_do_distribuido / 100
#  valor_do_imposto = preco_de_fabrica *  percentual_de_imposto / 100
#  preco_final =  preco_de_fabrica + lucro_do_distribuidor +  valor_do_imposto

#  ESCREVA lucro_do_distribuidor
#  ESCREVA valor_do_imposto
#  ESCREVA preco_final

#entrada
preço_fabr = float (input("Quanto custa o carro direto da fábrica: "))

percentual_do_dist = float (input("Qual a porcentagem do distribuidor: "))

percentual_do_imposto = float (input("Digite o valor do imposto: "))

#Procedimento
lucro_do_dist = preço_fabr * (percentual_do_dist / 100)

imposto = preço_fabr * (percentual_do_imposto / 100)

preço_final =  preço_fabr + lucro_do_dist + imposto

#saída
print  ("O lucro do distribuidor é: ",lucro_do_dist)

print  ("valor_do_imposto é: ",imposto)

print  ("O preço do carro será de: ",preço_final)
