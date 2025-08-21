opcaoMenu = 0
totalConta = 0

while opcaoMenu != 3:

    print('Opções:\n'
          '1 - Troca de óleo\n'
          '2 - Balanceamento\n'
          '3 - Sair')

    opcaoMenu = int(input("Digite uma opção: "))
    if opcaoMenu == 1:
        totalConta += 100
    if opcaoMenu == 2:
        totalConta += 70

print(f'Total conta: R$ {totalConta:.2f}')