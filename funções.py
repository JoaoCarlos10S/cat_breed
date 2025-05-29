def olamundo():
    print('ola mundo')

def olapessoa(nome):
    print(f'ola, {nome}')

def doblo(numero):
    return numero * 2
print(doblo(10))

def multiplicaDoisNumeros(a, b):
    return a * b

print(multiplicaDoisNumeros(5, 5))

x = 5 # Váriavel global
def soma():
    x = 10 # Váriavel local
    print(x)
    return x + 1
soma()
print(x)