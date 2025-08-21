velLeve = 50 * 1.1
velMedia = 70
velGrave = 90
velGravissima = 110

velVeiculo = float(input("Informe a velocidade que o veículo passou: "))

print("Sua velocidade foi de {velVeiculo} Km/h")
if velVeiculo > velGravissima:
    print("Infração gravíssima, 7 pontos na carteira.")
elif velVeiculo > velGrave:
    print("Infração grave, 5 pontos na carteira.")
elif velVeiculo > velMedia:
    print("Infração média, 4 pontos na carteira.")
elif velVeiculo > velLeve:
    print("Infração leve, 3 pontos na carteira.")
else:
    print("Isento da multa.")