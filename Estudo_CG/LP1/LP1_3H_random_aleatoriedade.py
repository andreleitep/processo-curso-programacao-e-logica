from random import randint

aleatMin = randint(1, 100)
aleatMax = randint(1, 100)
while aleatMin >= aleatMax:
    aleatMin = randint(1, 100)
    aleatMax = randint(1, 100)

passoAleat = randint(1,5)

print('min =', aleatMin)
print('max =', aleatMax)
print('passo =', passoAleat)


for i in range(aleatMin, aleatMax+1, passoAleat):
    print(i)