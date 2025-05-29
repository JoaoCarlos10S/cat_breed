print('Olá, sou John seu assistente burro, faça uma pergunta')

comando = input('Faça uma pergunta: ')
match comando:
    case 'nome'  |  'name':
        print('Neymar JR')
    case 'idade'  |  'quantos anos':
        print('35')
    case 'tempo':
        print('frio')
    case _:
        print('Não entendi')


