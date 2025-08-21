nota1 = float(input('Escreva a nota 1: '))
nota2 = float(input('Escreva a nota 2: '))
nota3 = float(input('Escreva a nota 3: '))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print('você passou com a média', media)
elif media < 5:
    print("Você reprovou com a média:", media)
else:
    print('Você reprovou com a média:', media)