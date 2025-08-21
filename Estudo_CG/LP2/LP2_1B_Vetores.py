vetorNomes = []
vetorIdades = []

for i in range(5):
    vetorNomes.append(input(f"Nome do {i+1}º participante: "))
    vetorIdades.append(int(input(f"Idade do {i+1}º participante: ")))

for i in range(5):
    print(f"{vetorNomes[i]} tem {vetorIdades[i]} anos de idade.")