altura = float(input("Informe sua altura: "))
peso = float(input("Informe seu peso: "))

imc = peso * altura ** 2

if imc < 18:
    print(f'imc = {imc}, abaixo do peso.')
elif imc < 24:
    print(f'imc = {imc}, peso ideal')
else:
    print(f'imc = {imc}, acima do peso')

