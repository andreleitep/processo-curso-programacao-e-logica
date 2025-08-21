nota1 = float(input('Escreva a nota 1: '))
nota2 = float(input('Escreva a nota 2: '))
nota3 = float(input('Escreva a nota 3: '))

media = (nota1 + nota2 + nota3) / 3

print('média:', media)

if media < 7:
    print('Você está de recuperação.')
else:
    print('Você está aprovade.')