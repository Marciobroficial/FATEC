# 23.Faça um programa que:
# leia um valor N inteiro e positivo
# Calcule e mostre o valor de E, conforme a fórmula:
# E =  1+11!+12!+13!+14!+...+1N!



for c in range(2, 10):
    m = 0
    while m <= 10:
        print("{} x {:2} = {:2}".format(c, m, c*m))
        m += 1
    print("-" * 15)