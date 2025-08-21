vetorNomes = ['andre', 'alex', 'giovanna', 'raisa', 'vino', 'giovanna']

pesquisa = input("Digite o nome a pesquisar: ")
pesquisa = pesquisa.lower()

# Resolução do professor

i = 0
posicao = 0
encontrado = False
while i < len(vetorNomes):
    if pesquisa == vetorNomes[i]:
        encontrado = True
        posicao = i + 1
    i += 1

print(f'Encontrado na {posicao}ª posição.' if encontrado else 'Não encontrado')

#=====================================================================

print('-' * 40)

i = 0

while True:
    if pesquisa == vetorNomes[i]:
        print(f"Valor encontrado: {pesquisa} é o {i+1}º valor.")
        break
    i += 1
    if i > 4:
        print(f"Valor {pesquisa} não encontrado")
        break

print('-' * 40)

for i in vetorNomes:
    if i == pesquisa:
        print(f'Valor {pesquisa} encontrado!')

print('-' * 40)

if pesquisa in vetorNomes:
    print(f'valor {pesquisa} encontrado.')
else:
    print(f'valor {pesquisa} não encontrado')