# 24.Faça um programa para calcular a tabuada do 2 até a do 9. USE DUAS ESTRUTURAS DE REPETIÇÃO

# for n in range (2,10):
#     print("*"*11)
#     for r in range (1,11):
#         print (n,'X',r,'=',n*r)

n = 1
while n <=9:
    n +=1 
    r = 0
    print('-'*15)
    while r <=10:
        print ( "{} x {:3} = {:3}".format ( n , r, n * r ))
        r +=1


    
       




