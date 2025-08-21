vetor1 = []
vetor2 = []
for i in range(0, 101, 10):
    vetor1.append(i)

j = len(vetor1) - 1
while j >= 0:
    vetor2.append(vetor1[j])
    j -= 1

print(vetor1)
print(vetor2)

opcao = input("1 - soma, 2 - subtração, 3 - multiplicação, 4 - divisão, 0 - sair: ")
while opcao != "0":
    j = 0
    vetor3 = []
    match opcao:
        case "1":
            while j < 10:
                vetor3.append(vetor1[j] + vetor2[j])
                j += 1
        case "2":
            while j < 10:
                vetor3.append(vetor1[j] - vetor2[j])
                j += 1
        case "3":
            while j < 10:
                vetor3.append(vetor1[j] * vetor2[j])
                j += 1
        case "4":
            while j < 10:
                vetor3.append(vetor1[j] / vetor2[j])
                j += 1
    print()
    print([i for i in vetor3], end = ' ')
    print('\n')
    opcao = input("1 - soma, 2 - subtração, 3 - multiplicação, 4 - divisão, 0 - sair: ")

print('\nFim do programa')