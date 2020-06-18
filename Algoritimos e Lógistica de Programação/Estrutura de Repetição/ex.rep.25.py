
# 25. Elabore um algoritmo que informada a idade de 10 nadadores
# o mesmo terá condições de classificar em uma das seguintes
# categorias: infantil = 5 - 10 anos; juvenil = 11-17 anos; adulto >= maiores de 18 anos. 
#---------------------------------------------------------------------------------------#
  
for nad in range(1,5):
    i = int(input(f"Qual a idade do nadador n° {nad} -> "))
    if i >= 5 and i <= 10:
        print("O nadador n°{} está na categoria Infantil".format(nad))
    if i > 10 and i <= 17:
        print("O nadador n°{} está na categoria Juvenil".format(nad))
    if i > 18:
        print("O nadador n°{} está na categoria Adulto".format(nad))