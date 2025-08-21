print('0, 11, 2')

for i in range(0, 11, 2):
    print(i, end=' ')

print('\n1, 11, 2')

for i in range(1, 11, 2):
    print(i, end=' ')

print('\n0, 10, 2')

for i in range(0, 10, 2):
    print(i, end=' ')

print('\n1, 10, 2')

for i in range(1, 10, 2):
    print(i, end=' ')

print('\n',list(range(11)), sep='')
print('\n',list(range(10, -1, -1)), sep='')

for i in range(10,-1, -1):
    print(i)