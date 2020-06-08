# 18. Faça um programa que receba duas notas de seis alunos. Calcule e mostre:
# a média aritmética das duas notas de cada aluno; e
# a mensagem que está na tabela a seguir:
# Média aritimética	Mesagem
# Até 3	Reprovado
# Entre 3 e 7	Exame
# De 7 para cima	Aprovado
# o total de alunos aprovados;
# o total de alunos de exame;
# o total de alunos reprovados;
# a média da classe.

reprovado = 0
exame = 0
aprovado = 0
somaMedia = 0

nAlunos = 1
while nAlunos <= 6:
    n1 = float(input("Digite a primeira nota do aluno ({}) -> ".format(nAlunos)))
    n2 = float(input("Digite a segunda nota do ({}) -> ".format(nAlunos)))

    media = (n1 + n2) / 2
    somaMedia += media
    mediaTotal = somaMedia / nAlunos
    print("A média do(a) aluno(a) {} foi {:.1f}".format(nAlunos, media))

    if media < 3:
        print("Reprovado")
        reprovado += 1
    if media >= 3 and media <=7:
        print("Exame")
        exame += 1
    if media > 7:
        print("Aprovado")
        aprovado += 1
    nAlunos += 1

print("\n{} alunos foram aprovados".format(aprovado))
print("{} alunos ficaram de exame".format(exame))
print("{} alunos foram reprovados".format(reprovado))
print("A média da sala foi {:.1f}".format(mediaTotal))