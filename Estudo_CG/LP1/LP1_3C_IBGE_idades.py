data_base = {}
nome = input("Digite o nome do participante: ")
maisVelhe = ''
maisNove = ''
menores = 0
soma_idades = 0
while nome:
    idade = int(input(f"Digite a idade de {nome}: "))
    if maisNove == '' or idade < data_base[maisNove]:
        maisNove = nome
    if maisVelhe == '' or idade > data_base[maisVelhe]:
        maisVelhe = nome
    if idade < 18:
        menores += 1
    soma_idades += idade
    data_base[nome] = idade
    nome = input("Digite o nome do participante: ")

pct_menores = menores / len(data_base) * 100
media_idades = soma_idades / len(data_base)

print(data_base)
print(f'mais velhe é {maisVelhe}, com {data_base[maisVelhe]} anos de idade')
print(f'mais nove é {maisNove}, com {data_base[maisNove]} anos de idade')
print(f'{pct_menores:.1f}% de participantes são menores de idade.')
print(f'A média de idade de participantes é {media_idades:.1f}')
