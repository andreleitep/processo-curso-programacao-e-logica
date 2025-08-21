numero1 = int(input("Escreva um número: "))
numero2 = int(input("Escreva um número: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

s = '{}\n   {}\n   {}\n   {}'
print(s.format(soma, subtracao, multiplicacao, divisao))