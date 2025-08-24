lado1, lado2, lado3 = 0, 0, 0

def ler_dados(): #procedimento
    # START
    global lado1, lado2, lado3
    lado1 = float(input("escreva lado 1: "))
    lado2 = float(input("escreva lado 2: "))
    lado3 = float(input("escreva lado 3: "))
    # END;

def verificarIntegridadeTriangulo():
    global lado1, lado2, lado3
    if lado1 > lado2 + lado3 or lado2 > lado1 + lado3 or lado3 > lado2 + lado1:
        return False
    else:
        return True

def verificarTipoTriangulo():
    # START
    if lado1 == lado2 == lado3:
        return "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "Isóceles"
    elif lado1 ** 2 == lado2 ** 2 + lado3 ** 2 or lado2 ** 2 == lado1 ** 2 + lado3 ** 2 or lado3 ** 2 == lado1 ** 2 + lado2 ** 2:
        return "Retângulo"
    else:
        return "Escaleno"
    # END;

# START

ler_dados()
if verificarIntegridadeTriangulo():
    print("Triângulo", verificarTipoTriangulo())
else:
    print("Não é um triângulo.")

# END.