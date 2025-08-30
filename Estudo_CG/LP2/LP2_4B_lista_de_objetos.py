class cadastroCliente:
    def __init__(self, nome, rg, idade):
        self.nome = nome
        self.rg = rg
        self.idade = idade

clientes = ['', '', '']
opcao_menu = 0

def menu():
    global opcao_menu
    print("Escolha uma das opções: ")
    print("    1 - Cadastrar")
    print("    2 - Pesquisar")
    print("    3 - Sair")
    opcao_menu = input("Digite: ")


menu()
flag = 0

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
                    print(f'Cliente cadastrado na posição {i + 1}')
                    break
        case "2":
            pesq = input("Digite o que quer pesquisar: ")
            for i in range(3):
                if clientes[i]:
                    if clientes[i].nome == pesq:
                        print(f"'{pesq}' encontrado na posição {i + 1}.")
                        flag = 1

            if not flag:
                print(f"'{pesq}' não encontrado.")
    flag = 0
    menu()

for i in range(len(clientes)):
    if clientes[i]:
        print(f'{clientes[i].nome} do RG {clientes[i].rg} tem {clientes[i].idade} anos')