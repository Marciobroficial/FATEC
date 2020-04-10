24. Dados três valores X, Y e Z, verifique se eles podem ser os comprimentos dos lados de um triângulo e, se forem, verifique se é um triângulo equilátero, isósceles ou escaleno. Se eles não formarem um triângulo, escreva uma mensagem.
Considere que:

o comprimento de cada lado de um triângulo é menor que a soma dos outros dois lados;
chama-se equilátero o triângulo que tem três lados iguais;
denomina-se isósceles o triângulo que tem o comprimento de dois lados iguais;
recebe o nome de escaleno o triângulo que tem os três lados diferentes.

LEIA x, y, z

SE x < y + z E y < x + z E z < x + y
    SE x = y E y = z
        ESCREVA “Triângulo Equilátero”
    SENÃO SE x = y OU x = z OU y = z
        ENTÃO ESCREVA “Triângulo Isósceles”
    SENÃO SE x ≠ y E x ≠ z E y ≠ z
        ENTÃO ESCREVA “Triângulo Escaleno”
SENÃO
    ESCREVA “Essas medidas não formam um triângulo”