#####################################################################################################################
# 9. Faça um programa que receba três notas de um aluno,
# calcule e mostre a média aritmética e a mensagem constante na tabela a seguir.
# Aos alunos que ficaram para exame, calcule e mostre a nota que deverão
# tirar para serem aprovados, considerando que a média exigida é 6,0.
#
#   MÉDIA ARITMÉTICA	    MENSAGEM
#   0,0 <= média < 3,0	    Reprovado
#   3,0 <= média < 7,0	    Exame
#   7,0 <= média <= 10,0	Aprovado
#
#  SE media >= 3 E media < 7
#     ESCREVA “Exame”
#     nota_exame = 12 - media
#     ESCREVA “Deve tirar nota”, nota_exame, “para ser aprovado”
#
######################################################################################################################
print('<->'*35)
print()
nt1 = float (input ('Digite a primeira nota: '))
nt2 = float (input ('Digite a segunda nota: '))
nt3 = float (input ('Digite a terceira nota: '))
md = (nt1 + nt2 + nt3) / 3
if md >= 0 and md <= 3:
    print ('Média:',md ,'Reprovdo')
elif md >= 3.0 and md <= 7:
    print ('Média: ',md ,'Exame')
    n_e = 12 - md
    print ('Deve tira:',n_e , 'Para ser Aprovado')
else:
    print ('Média: ',md , 'Aprovado: ')
print()
print('<->'*35)    
#########################################################################################################################   
