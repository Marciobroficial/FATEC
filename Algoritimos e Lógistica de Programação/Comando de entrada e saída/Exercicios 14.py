#14. Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
#a idade dessa pessoa;
#quantos anos ela terá em 2050.
#LEIA ano_atual
#LEIA ano_nascimento
#idade_atual = ano_atual − ano_nascimento
#idade_2050 = 2050 − ano_nascimento
#ESCREVA idade_atual

#entrada
ano = int (input("Digite o ano atual: "))

nasc = int (input("Digite sua data de nascimento: "))

#processamento 
idade_atual =  ano - nasc

i2050 = 2050 - nasc

#saida
print ("A ideade atual é: ",idade_atual)

print ("em 2050 ela estará com: ",i2050)