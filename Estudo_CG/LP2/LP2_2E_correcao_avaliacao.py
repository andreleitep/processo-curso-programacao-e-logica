gabarito = [0,1,2,3,4,5,6,7,8,9]
opcao_menu = ''
notaFinal = 0

def mostrar_menu(): #procedimento
    #START
    global opcao_menu
    print("1 - Cadastrar Gabarito")
    print("2 - Cadastrar Prova")
    print("3 - Sair")
    opcao_menu = input("Escolha uma das opções: ")
    #END;

def cadastrarGabarito():
    global gabarito
    for i in range(10):
        gabarito[i] = input(f"Informe a resposta da questão {i+1}: ")

def cadastrarProva(): #float (função que retorna real)
    #START
    global gabarito
    nota = 0
    for i in range(10):
        resposta = input(f"Escreva a resposta para a questão {i+1}: ")
        if resposta == gabarito[i]:
            nota += 1
        #fimse
    #fimpara
    return nota
    #END;

def verificarSituacao(nota):
    if nota >= 7:
        print(f'nota {nota}: Aprovado!')
    elif 2 <= nota < 7:
        print(f'nota {nota}: Recuperação!')
    else:
        print(f'nota {nota}: Reprovado!')


mostrar_menu()
while opcao_menu != "3":
    match opcao_menu:
        case "1":
            cadastrarGabarito()
        case "2":
            notaFinal = cadastrarProva()
            verificarSituacao(notaFinal)

    mostrar_menu()