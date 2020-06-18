# 15. Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
# nome da cidade;
# número de veículos de passeio;
# número de acidentes de trânsito com vítimas.
# Deseja-se saber:

# o maior índice de acidentes de trânsito e a que cidades pertence;
# o menor índice de acidentes de trânsito e a que cidades pertence;
# qual é a média de veículos nas cinco cidades juntas;
# qual é a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
# ALGORITMO
# total_de_cidades_pesquisadas = 5
# somatoria_dos_veiculos_nas_cidades = 0
# somatoria_dos_acidentes_nas_cidades_com_mais_de_2000_veiculos = 0
# numero_de_cidades_com_mais_de_200_veiculos = 0
 
# PARA cidade NO INTERVALO total_de_cidades_pesquisadas
#     LEIA nome_da_cidade, numero_de_veiculos, numero_de_acidentes
#     SE cidade == 0
#         maior_casos_de_acidentes = numero_de_acidentes
#         cidade_com_maior_casos_de_acidentes = nome_da_cidade
#         menor_casos_de_acidentes = numero_de_acidentes
#         cidade_com_maior_casos_de_acidentes = nome_da_cidade
#     SENÃO
#         SE numero_de_acidentes > maior_casos_de_acidentes
#              maior_casos_de_acidentes = numero_de_acidentes
#              cidade_com_maior_casos_de_acidentes = nome_da_cidade
#         SE numero_de_acidentes < menor_casos_de_acidentes
#             menor_caso_de_acidentes = numero_de_acidentes
#             cidade_com_maior_casos_de_acidentes = nome_da_cidade
 
#     somatoria_dos_veiculos_nas_cidades += numero_de_veiculos
 
#     SE numero_de_veiculos > 2000
#         soma_dos_acidentes_nas_cidades_acima_de_2000_veiculos += numero_de_acidentes
#         numero_de_cidades_com_mais_de_200_veiculos += 1
 
# media_de_carros_nas_cidades = somatoria_dos_veiculos_nas_cidades / total_de_cidades_pesquisadas
 
# SE numero_de_cidades_com_mais_de_200_veiculos == 0
#     ESCREVA “Não foi informada nenhuma cidade com menos de 2000 veículos”
# SENAO
#     media_de_acidentes_nas_cidade_com_mais_de_2000_veiculos = soma_dos_acidentes_nas_cidades_acima_de_2000_veiculos /  numero_de_cidades_com_mais_de_200_veiculos
 
#     ESCREVA nome_da_cidade, cidade_com_maior_casos_de_acidentes
#     ESCREVA nome_da_cidade, maior_casos_de_acidentes 
#     ESCREVA media_de_carros_nas_cidades
#     ESCREVA media_de_acidentes_nas_cidade_com_mais_de_2000_veiculos
#----------------------------------------------------------------------------------------------------------------------#


totalCidadePesquisadas = 5
somaVeiculosCidade = 0
somaAcidentesCidadesMais2000 = 0
numeroAcidenteMais200 = 0
numeroAcidenteMais200 = 0
mediaAcidentesCidadesMais2000 = 0
maiorCasoAcidentes = 0
menorCasoAcidentes = 30000

for c in range(totalCidadePesquisadas):
    nomeCidade = str(input("Digite o nome da cidade n° {} -> ".format(c)))
    numeroVeiculos = int(input("Digite o número de veículos que transitam na cidade -> "))
    numeroAcidentes = int(input("Digite o número de acidentes ocorridos nessa cidade -> "))
    if numeroAcidentes == 0:
        maiorCasoAcidentes = numeroAcidentes
        cidadeMaiorCasosAcidentes = nomeCidade
        menorCasoAcidentes = numeroAcidentes
        cidadeMenorCasosAcidentes = nomeCidade
    else:
        if numeroAcidentes > maiorCasoAcidentes:
            maiorCasoAcidentes = numeroAcidentes
            cidadeMaiorCasosAcidentes = nomeCidade
        if numeroAcidentes < menorCasoAcidentes:
            menorCasoAcidentes = numeroAcidentes
            cidadeMenorCasosAcidentes = nomeCidade

    somaVeiculosCidade += numeroVeiculos

    if numeroVeiculos > 2000:
        somaAcidentesCidadesMais2000 += numeroAcidentes
        numeroAcidenteMais200 += 1

mediaCarrosCidades = somaVeiculosCidade / totalCidadePesquisadas

if numeroAcidenteMais200 == 0:
    print("Não foi informada nenhuma cidade com menos de 2000 veículos.")
else:
    mediaAcidentesCidadesMais2000 = somaAcidentesCidadesMais2000 / numeroAcidenteMais200
print("A cidade que contém maior número de acidentes é: {}".format(cidadeMaiorCasosAcidentes))
print("A cidade que contém menor número de acidentes é: {}".format(cidadeMenorCasosAcidentes))
print("A média de carros na cidade é de: {:.0f} carros".format(mediaCarrosCidades))
print("A média de acidentes nas cidades com mais de 2000 carros foi de: {:.0f}".format(mediaAcidentesCidadesMais2000))