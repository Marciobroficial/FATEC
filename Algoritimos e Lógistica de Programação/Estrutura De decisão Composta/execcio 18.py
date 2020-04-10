18. Faça um programa que receba o código correspondente ao cargo de um funcionário e seu salário atual e mostre o cargo, o valor do aumento e seu novo salário. Os cargos estão na tabela a seguir.
CÓDIGO	CARGO	PERCENTUAL
1	Escriturário	50%
2	Secretário	35%
3	Caixa	20%
4	Gerente	10%
5	Diretor	Não tem aumento
SE cargo == 1
    ESCREVA “O cargo é Escriturário”
    aumento = salario * 50 / 100
    ESCREVA “O valor do aumento é: “, aumento
    novo_sal = salario + aumento
    ESCREVA “O novo salário é: “, novo_sal
SENÃO SE cargo == 2
    ESCREVA “O cargo é Secretário”
    aumento = salario * 35 / 100
    ESCREVA “O valor do aumento é: “, aumento
    novo_sal = salario + aumento
    ESCREVA “O novo salário é: “, novo_sal]
SENÃO SE cargo == 3
    ESCREVA “O cargo é Caixa”
    aumento = salario * 20 / 100
    ESCREVA “O valor do aumento é: “, aumento
    novo_sal = salario + aumento
    ESCREVA “O novo salário é: “,novo_sal
SENÃO SE cargo == 4
    ESCREVA “O cargo é Gerente”
    aumento = salario * 10 / 100
    ESCREVA “O valor do aumento é: “, aumento
    novo_sal = salario + aumento
    ESCREVA “O novo salário é: “, novo_sal
SENÃO SE cargo == 5
    ESCREVA “O cargo é Diretor”
    aumento = salario * 0 / 100
    ESCREVA “O valor do aumento é: “, aumento
    novo_sal = salario + aumento
    ESCREVA “O novo salário é: “, novo_sal