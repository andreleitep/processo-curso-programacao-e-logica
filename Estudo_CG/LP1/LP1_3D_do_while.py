senha = "python"
cont = 0

while True:
    palavra = input("Escreva a senha: ")
    if palavra == senha:
        print("Acesso permitido.")
        break
    if palavra != senha:
        print("Acesso negado.")
        cont += 1
    if cont > 4:
        print("Conta bloqueada.")
        break