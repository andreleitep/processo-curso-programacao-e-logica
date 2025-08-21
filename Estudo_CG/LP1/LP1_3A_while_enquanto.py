class Pessoa:
    def __init__(self,nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
    def exibe(self):
        print(f'nome: {self.nome}')
        print(f'    idade: {self.idade}')
        print(f'    altura: {self.altura:.2f}')

joao = Pessoa('João', 8, 1.05)
marcelo = Pessoa('Marcelo', 8, 1.20)

print('=' * 40)
joao.exibe()
print('-' * 30)
marcelo.exibe()
while joao.altura < marcelo.altura:
    joao.altura += 0.07
    marcelo.altura += 0.05
    joao.idade += 1
    marcelo.idade += 1

    print('=' * 40)
    joao.exibe()
    print('-' * 30)
    marcelo.exibe()
print('=' * 40)