from LP2_4A_orientacao_a_objetos import cadastroCliente

clientes = ['','','']
opcao_menu = 0

def menu():
    global opcao_menu
    print("Escolha uma das opções: ")
    print("    1 - Cadastrar")
    print("    2 - Pesquisar")
    print("    3 - Sair")
    opcao_menu = input("Digite: ")

menu()

while opcao_menu != "3":
    match opcao_menu:
        case "1":
            for i in range(3):
                if clientes[i] == '':
                    nome = input("Nome: ")
                    rg = input("RG: ")
                    idade = int(input("Idade: "))
                    client = cadastroCliente(nome, rg, idade)
                    clientes[i] = client
                    print(f'Cliente cadastrado na posição {i+1}')
                    break
        case "2":
            pesq = input("Digite o que quer pesquisar: ")
            for i in range(3):
                if clientes[i]:
                    if clientes[i].nome == pesq:
                        print(f"{pesq} encontrado na posição {i+1}.")
                        break
                print(f"'{pesq}' não encontrado.")

for i in range(len(clientes)):
    print(f'{clientes[i].nome} do RG {clientes[i].rg} tem {clientes[i].idade} anos')