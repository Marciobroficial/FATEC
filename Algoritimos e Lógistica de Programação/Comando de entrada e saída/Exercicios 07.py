#ENTRADA DE DADOS

base = float (input('QUal o salario base do funcionário: '))
caculoimpo = float (input('qual o percetual sobre o salário base: '))

#PROCESSAMENTO

imposto = base * caculoimpo / 100
salario_a_receber = base + 50 - imposto

#SAIDA

print ('Receberá de Salério: ',salario_a_receber)