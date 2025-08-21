# ctrl + f8 = breakpoint
# f8 roda o programa linha a linha, no debug se houver um breakpoint
# f7 roda internamente (talvez dentro de funções, métodos, não sei)
#       shift + f8 sai da função que você entrou com o f7

def funcao():
    print('rodando1')
    print('rodando2')
    print('rodando3')
    print('rodando4')
    print('rodando5')

exemplo = 20
var = exemplo + 20
print(exemplo, var)
print('principal1')
print(exemplo, var)
print('principal2')
print('principal3')
funcao()
print('principal4')
print('principal5')
funcao()
print('principal6')
print('principal7')
print('principal8')