lado1 = float(input("Lado 1: "))
lado2 = float(input("Lado 2: "))
lado3 = float(input("Lado 3: "))

if (lado1 > lado2 + lado3) or (lado2 > lado1 + lado3) or (lado3 > lado1 + lado2):
    print('Não é um triângulo.')
else:
    if lado1 == lado2 == lado3:
        print('Triângulo equilátero')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('Triângulo isóceles')
    else:
        print('Triângulo escaleno')