teste = 0
def proce_somar(a, b): # procedimento
    global teste
    teste = a + b

def func_somar(a, b):
    return a + b

def testar():
    return func_somar(50, 50) + 40

proce_somar(10, 20)
print(teste)
print('-' * 40)
print(func_somar(10,20))
print('-' * 40)
testar()
