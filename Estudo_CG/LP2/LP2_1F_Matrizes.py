cinema = [[],[],[],[],[]]
for i in cinema:
    for j in range(10):
        i.append('0')

fil_cad = input("Cadeira e fileira separado por espaço: ")
if fil_cad != '0':
    fil_cad = fil_cad.split()
    fileira = int(fil_cad[0])
    cadeira = int(fil_cad[1])

while fil_cad != '0':
    if cinema[fileira - 1][cadeira - 1] == '0':
        print("Cadeira selecionada com sucesso")
        cinema[fileira - 1][cadeira - 1] = 'X'
    else:
        print("Cadeira ocupada.")

    fil_cad = input("Cadeira e fileira separado por espaço: ")
    if fil_cad != '0':
        fil_cad = fil_cad.split()
        fileira = int(fil_cad[0])
        cadeira = int(fil_cad[1])

cont = 1
print('    1  2  3  4  5  6  7  8  9  10')
print('  ┌─┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┐')
for i in cinema:
    print(cont, '│', end=' ')
    for j in i:
        print(j,end='  ')
    print('│')
    cont += 1
print('  └───────────────────────────────┘')