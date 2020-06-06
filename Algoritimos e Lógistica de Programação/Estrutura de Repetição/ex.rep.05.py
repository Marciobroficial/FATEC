# 5. Faça um algoritmo que calcule e mostre a tabuada do 5.
#############################################################
print()
tab = 1
while tab <= 10:
    print("{} x {:2} = {:2}".format (5, tab, 5*tab))
    tab += 1
print()
n = int(input("Você gostaria de ver a tabuada de qual número? "))
print()
for x in range(11):
    print("{} x {:2} = {:2}".format(n, x, n * x))   

