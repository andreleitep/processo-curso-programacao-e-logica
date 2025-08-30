# Conceito de Herança

class Pessoa:
    def __init__(self, nome, dataNasc):
        self.nome = nome
        self.dataNasc = dataNasc

class pessoaFisica(Pessoa):
    def definir(self, cpf, rg):
        self.cpf = cpf
        self.rg = rg

class pessoaJuridica(Pessoa):
    def definir(self, cnpj, ie):
        self.cnpj = cnpj
        self.ie = ie

andre = pessoaFisica('Andre', '02/06/1994') # atributos da classe mãe
andre.definir(41773702823, 370090380)

print(andre.nome, andre.dataNasc, andre.cpf, andre.rg)