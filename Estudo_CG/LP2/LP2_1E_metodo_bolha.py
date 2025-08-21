from random import randint

vetor1 = []
aux = 0

for i in range(10):
    vetor1.append(randint(0, 100))

print(vetor1)

for i in range(len((vetor1))):
    for j in range(len((vetor1))):
        if vetor1[j] > vetor1[i]:
            aux = vetor1[i]
            vetor1[i] = vetor1[j]
            vetor1[j] = aux
            # vetor[i], vetor[j] = vetor[j], vetor[i]

print(vetor1)