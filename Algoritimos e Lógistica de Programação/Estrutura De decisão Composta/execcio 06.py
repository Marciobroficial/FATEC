# 6. Um banco concederá um crédito especial aos seus clientes, variável com o saldo médio no último ano.
# Faça um algoritmo que leia o saldo médio de um cliente e calcule o valor do crédito de acordo com a tabela a seguir.
# Mostre uma mensagem informando o saldo médio e o valor do crédito.

  # Saldo médio
   # * de 0 a 200 nenhum crédito
   # * de 201 a  400 20% do valor do saldo médio
   # * de 401 a  600 30% do valor do saldo médio
   # * acima de 601 40% do valor do saldo médio

# Entrada
sm = float (input('Digite o saldo medio do ultimo ano: '))
if sm >=0 and sm <=200:
  print ('Crédito Negado')
elif sm > 201 and sm >= 400:
  credito = sm * 20/100
  print ('Seu crédito será de:',credito)
elif sm > 401 and sm >= 600:
  credito = sm * 30/100
  print ('Seu crédito é de:',credito)
else:
  credito = sm * 40/100
  print ('Seu credito será de:',credito)