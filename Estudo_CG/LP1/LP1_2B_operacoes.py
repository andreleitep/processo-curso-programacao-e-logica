x = 10
y = 3
w = x + y
print(w)
w = x - y
print(w)
w = x * y
print(w)
w = x / y
print(w)
w = x // y
print(w)
w = x % y
print(w)

teste = int(input("Escreva um número: "))
if teste % 2 == 0:
    print(f'{teste} é par')
else:
    print(f'{teste} é ímpar')