# 18. Faça um programa que receba o código correspondente ao cargo de um funcionário
# e seu salário atual e mostre o cargo, o valor do aumento e seu novo salário. Os cargos estão na tabela a seguir.
# CÓDIGO	CARGO	        PERCENTUAL
# 1	        Escriturário	50%
# 2	        Secretário	    35%
# 3	        Caixa	        20%
# 4	        Gerente	        10%
# 5	Diretor	Não tem aumento

# SE cargo == 1
#    ESCREVA “O cargo é Escriturário”
#    aumento = salario * 50 / 100
#    ESCREVA “O valor do aumento é: “, aumento
#    novo_sal = salario + aumento
#    ESCREVA “O novo salário é: “, novo_sal
# SENÃO SE cargo == 2
#    ESCREVA “O cargo é Secretário”
#    aumento = salario * 35 / 100
#    ESCREVA “O valor do aumento é: “, aumento
#    novo_sal = salario + aumento
#    ESCREVA “O novo salário é: “, novo_sal
# SENÃO SE cargo == 3
#    ESCREVA “O cargo é Caixa”
#    aumento = salario * 20 / 100
#    ESCREVA “O valor do aumento é: “, aumento
#    novo_sal = salario + aumento
#    ESCREVA “O novo salário é: “,novo_sal
# SENÃO SE cargo == 4
#    ESCREVA “O cargo é Gerente”
#    aumento = salario * 10 / 100
#    ESCREVA “O valor do aumento é: “, aumento
#    novo_sal = salario + aumento
#    ESCREVA “O novo salário é: “, novo_sal
# SENÃO SE cargo == 5
#    ESCREVA “O cargo é Diretor”
#    aumento = salario * 0 / 100
#    ESCREVA “O valor do aumento é: “, aumento
#    novo_sal = salario + aumento
#    ESCREVA “O novo salário é: “, novo_sal
###############################################################################################
print ( '<->' * 35)
print ( '\nMeunu de opções:\n \nnº 1. Contador 50% \nnº 2. Secretário 35% \nnº 3. Funcionário bancário 20% \nnº 4. Gerente 10% \nnº 5. Diretor Sem aumento de pagamento' )

opção  =  int ( input ( '\nDigite uma das opções do menu de acordo com a sua posição :> ' ))
salários = int ( input ('Digite o seu salário atual?:> R$: ' ))

if  opção  ==  1 :
    print ( '\nA posição é Escriturário' )
    sal_base  =  salários  *  50  /  100
    print ( 'O aumento salarial é: R$: {:.2f}\n'.format ( sal_base ))
    print ( 'O novo salário é de: R$: {:.2f}\n' .format ( salários  +  sal_base ))
    print ( '<->' * 35)
elif opção ==  2 :
    print ( 'O cargo é Secretário' )
    sal_base  =  salários  *  35  /  100
    print ( 'O aumento salarial é: R$: {:.2f}\n'.format ( sal_base ))
    print ( 'O novo salário é de: R$: {:.2f}\n' .format ( salários  +  sal_base ))
    print ( '<->' * 35)
elif opção ==  3 :
    print ( '\nA posição é Caixa' )
    sal_base  =  salários  *  20  /  100
    print ( 'O aumento salarial é: R$: {:.2f}\n'.format ( sal_base ))
    print ( 'O novo salário é de: R$: {:.2f}\n' .format ( salários  +  sal_base ))
    print ( '<->' * 35)
elif opção ==  4 :
    print ( '\nA posição é Gerente' )
    sal_base  =  salários  *  10  /  100
    print ( 'O aumento salarial é: R$: {:.2f}\n'.format ( sal_base ))
    print ( 'O novo salário é de: R$: {:.2f}\n' .format ( salários  +  sal_base ))
    print ( '<->' * 35)
elif opção ==  5 :
    print ( '\nO cargo é Diretor' )
    print ( 'Não há aumento de salário porque você é diretor.!\n' )
else :
    print ( '\nOpção inválida!\n' )
    print ( '<->' * 35 )
