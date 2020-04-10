#Entrada de dados

deposito = float (input('valor do deposito: '))
taxa = float (input('valor da taxa: '))

#Processamento

rendimento = deposito * taxa / 100
total = deposito + (rendimento * 30)

#Saida de dados

print ('rendimento: ',rendimento)
print ('total: ',total)
