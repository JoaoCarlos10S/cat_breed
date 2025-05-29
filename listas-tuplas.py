import os

tarefas = []

def adicionaTarefa(tarefa):
    novaTarefa = (tarefa, "pendente")
    tarefas.append(novaTarefa)

def exibeTarefas():
    if not tarefas:
        print('A lista está vazia')
        return
    for tarefa in tarefas:
        print(f'{tarefa[0]} - status: {tarefa[1]}')

def concluirTarefa(tarefa):
    global tarefas
    tarefas = [ (t[0], 'concluído') if t[0] == tarefa else t for t in tarefas ]
    
def removerTarefa(tarefa):
    global tarefas
    tarefas = [ t for t in tarefas if t[0] != tarefa ]

def buscarTarefa(tarefa):
    resultado = [ t for t in tarefas if t[0].lower() == tarefa.lower() ]
    if resultado:
        for titulo, status in resultado:
            print(f'Encontrada: {titulo} - Status: {status}')
    else:
        print(f'Tarefa não encontrada: {tarefa}')

while True:
    os.system('cls')

    print('Boas vindas ao gerenciador de lista de tarefas')
    print()
    print('O que fazer agora')
    print('1 - Listar tarefas')
    print('2 - Adionar tarefas')
    print('3 - Remover tarefa')
    print('4 - Marcar tarefa como concluída')
    print('5 - Buscar tarefa')
    print('0 - Sair')
    opcao = int(input('Digite uma opção: '))

    match opcao:
        case 1:
            exibeTarefas()
        case 2:
            tarefa = input('Digite uma tarefa: ')
            adicionaTarefa(tarefa)
        case 3:
            tarefa = input('Digite tarefa: ')
            removerTarefa(tarefa)
        case 4:
            tarefa = input('Digite tarefa: ')
            concluirTarefa(tarefa)
        case 5:
            tarefa = input('Digite a tarefa: ')
            buscarTarefa(tarefa)
        case 0:
            break
        case _:
            print('Opção inválida')
    print()
    input('Pressione ENTER para continuar...')
    





