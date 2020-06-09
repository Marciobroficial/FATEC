# 20. Foi feita uma pesquisa com as crianças de uma determinada localidade. Faça um programa que:
# leia o número de crianças nascidas no período;
# identifique o sexo (M ou F) e a idade da criança.
# O programa deve calcular e mostrar:

# a percentagem de crianças do sexo marculino;
# a percentagem de crianças do sexo feminino;
# a percentagem de crianças menores que 24 meses.
# **Observação:

# porcentagem_de_meninos = total_de_meninos / total_de_criancas_nascidas * 100

# porcentagem_de_meninas = total_de_meninas / total_de_criancas_nascidas * 100 porcentagem_de_criancas_menores_de_24_mese=criancas_menores_de_24_mese/total_de_criancas_nascidas*100
#######################################################################################################
masc = 0
fem = 0
cri_menores = 0
por_meninos = 0
por_meninas = 0
por_crianças = 0
x = 1
while (x != 0):     
     idade = int(input("Digite a idade em meses: "))
     sexo = input("Digite seu sexo: (M ou F) ") 
     if idade < 24: 
        cri_menores = cri_menores + 1     
     if sexo == "M" or sexo == "m":
        masc = masc + 1     
     if sexo == "F" or sexo == "f":
        fem = fem + 1 
     x = int(input('Digite 0 para encerrar ou 1 para continuar: '))        
     if x == 0:
           break
     else:
          x = x + 1 
total_c = masc + fem 
por_meninos = masc / total_c*100
por_meninas = fem / total_c*100
por_crianças = cri_menores/total_c*100 
print("A porgentagem de meninos é: {:.2f}".format (por_meninos))
print("A porgentagem de meninas é: {:.2f}".format (por_meninas))
print("A porgentagem de crianças é: {:.2f}".format (por_crianças))

