tabuleiro = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]

jogador = 'X'

# Função para fazer o tabuleiro

def exibeTabuleiro():
    for linha in tabuleiro:
        print(f'|'.join(linha))
        print('-' * 5)

# Função para chamar a jogada

def jogada(linha, coluna):
    if (
        not 0 <= linha <= 2 or
        not 0 <= coluna <= 2 or
        tabuleiro[linha][coluna] != ' '
    ):
        print('Jogada iválida')
        return jogador
    tabuleiro[linha][coluna] = jogador
    return 'O' if jogador == 'X' else 'X'


def temGanhador():
    """ Verificar as linhas """
    for linha in range(3):
        if (
            tabuleiro[linha][0] != ' ' and
            tabuleiro[linha][0] == tabuleiro[linha][1] and
            tabuleiro[linha][0] == tabuleiro[linha][2]
        ):
            print(f'{tabuleiro[linha][0]} GANHOU!!! ')
            return True

    """ Verificar as colunas """
    for linha in range(3):
        if (
            tabuleiro[0][coluna] != ' ' and
            tabuleiro[0][coluna] == tabuleiro[1][coluna] and
            tabuleiro[0][coluna] == tabuleiro[2][coluna]
        ):
            print(f'{tabuleiro[0][coluna]} GANHOU!!! ')
            return True

    """ Verificar as diagonais """
    if (
        tabuleiro[1][1] != ' ' and
        (
            (
                tabuleiro[0][0] == tabuleiro[1][1] and
                tabuleiro[0][0] == tabuleiro[2][2]
            ) or
            (
                tabuleiro[0][2] == tabuleiro[1][1] and
                tabuleiro[1][1] == tabuleiro[2][0]
            )
        )
    ):
        print(f'{tabuleiro[1][1]} GANHOU!!! ')
        return True

    """ Se não teve ganhador em nenhuma forma """
    return False

def temEmpate():
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == ' ':
                return False
    print('Acabou empatado! ')
    return True

# while True - função de repetição

while True:
    print(f'Jogador da vez:{jogador}')
    try:
        linha = int(input('Digite a linha: '))
        coluna = int(input('Digite a coluna: '))
        jogador = jogada(linha, coluna)
    except IndexError:
        print('Digite valores numéricos de 0 a 2')
    except ValueError:
        print('Os valore devem ser números inteiros')
    exibeTabuleiro()
    if temGanhador() or temEmpate():
        break
