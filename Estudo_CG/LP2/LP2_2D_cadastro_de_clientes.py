opcaoMenu = ""
clientes = ["","","","",""]
indiceSucesso = ""

def mostrarMenu():
    # START
    global opcaoMenu
    print('1 - Cadastrar')
    print('2 - Pesquisar')
    print('3 - Excluir')
    print('4 - Exibir')
    print('5 - Sair')
    opcaoMenu = input("Selecione: ")
    # END;

def cadastrar():
    # START
    for i in range(5):
        if clientes[i] == "":
            clientes[i] = input(f"Escreva o nome do cliente {i+1}: ")
    # END;

def pesquisar():
    # START
    global clientes
    indiceSucesso = -1
    i = 0
    nomeAPesquisar = input("Digite o nome que quer pesquisar: ")
    while i < len(clientes):
        if clientes[i] == nomeAPesquisar:
            indiceSucesso = i
        i += 1
    if indiceSucesso == -1:
        print("Cliente não encontrado.")
    else:
        print(f"Cliente {nomeAPesquisar} encontrado na linha {indiceSucesso + 1}")
    # END;

def excluir():
    global clientes
    indiceExclusao = int(input("Digite o índice do cliente a ser excluído: "))
    if 5 < indiceExclusao < 1:
        print("Índice inválido")
    else:
        clientes[indiceExclusao - 1] = ""

def exibir():
    global clientes
    for i in range(5):
        print(f"{f"{i+1} - {clientes[i]}":>50}")

#START
mostrarMenu()
while opcaoMenu != "5":
    match opcaoMenu:
        case "1":
            cadastrar()
        case "2":
            pesquisar()
        case "3":
            excluir()
        case "4":
            exibir()
        case _:
            print("Opção inválida.")
    mostrarMenu()