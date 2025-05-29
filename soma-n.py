soma = 0
n = 1

while n <= 1:
    soma = soma + n
    n = n + 1
    print(f'soma:  {soma}')
    print(f'n: {n}')

for index in range (1, 16):
    soma += index

# soma = sum([i for i in range(1,15)])
print(f'Á soma dos números de 1 a 15 é {soma}')