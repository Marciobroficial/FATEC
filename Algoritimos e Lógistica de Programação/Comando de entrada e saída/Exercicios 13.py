#13. Sabe-se que:  #pé = 12 polegadas  #1 jarda = 3 pés  #1 milha = 1,760 jarda
#Faça um programa que receba uma medida em pés, faça as conversões a seguir e mostre os resultados.

#Polegadas;

#Jardas;

#Milhas.

#LEIA pes
#polegadas = pes * 12
#jardas = pes / 3
#milhas = jardas / 1760
#ESCREVA polegadas, jardas, milhas

#Entrada de dados

p = float (input('Digite um valor em pé pra que seja convertido: '))

#Processamento

pol = p * 12
jar = p / 3
mil = jar / 1760

#Saida de dados

print ('o valor de pol: ',pol)

print ('o Valor de jar é: ',jar)

print ('O valor de mil é: ',mil)