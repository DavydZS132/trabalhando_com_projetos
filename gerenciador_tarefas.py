import os

gerenciador_tarefas = []

def mostrar_menu():
    print('1. Adicionar Tarefa')
    print('2. Visualizar Tarefas')
    print('3. Remover Tarefa')
    print('4. Sair')

def adicionar_tarefas():
    os.system('cls')
    print('Adicionar tarefas.')

    nome_tarefas = input('Digite a Tarefa: ').strip()

    gerenciador_tarefas.append(nome_tarefas)
    print('Tarefa Adicionada')

    input('Pressione ENTER para voltar ao menu...')

def listar_tarefas():
    if len(gerenciador_tarefas) == 0:
        print('Nenhuma Tarefa Cadastrada')
    else:
        for i, tarefas_adicionadas in enumerate(gerenciador_tarefas, start=1):
            print(f'{i} - {tarefas_adicionadas}')
    
    input('\nPressione ENTER para voltar ao menu...')

def excluir_tarefas():
    os.system('cls')
    print('Remover tarefa.\n')

    if len(gerenciador_tarefas) == 0:
        print('Nenhuma tarefa cadastrada.')
        input('\nPressione ENTER para voltar ao menu...')
        return

    for i, tarefa in enumerate(gerenciador_tarefas, start=1):
        print(f'{i} - {tarefa}')

    try:
        numero = int(input('\nDigite o número da tarefa que deseja remover: '))

        if 1 <= numero <= len(gerenciador_tarefas):
            tarefa_removida = gerenciador_tarefas.pop(numero - 1)
            print(f'Tarefa "{tarefa_removida}" removida com sucesso!')
        else:
            print('Erro: Número de tarefa inválido.')

    except ValueError:
        print('Erro: Entrada inválida! Digite um número.')

    input('\nPressione ENTER para voltar ao menu...')


def escolher_opcao():
    try:
        opcao = int(input('Digite uma opção: '))

        if opcao == 1:
            adicionar_tarefas()
        elif opcao == 2:
            listar_tarefas()
        elif opcao == 3:
            excluir_tarefas()
        elif opcao == 4:
            print('Saindo do gerenciador de tarefas. Até mais!')
            return False
        else:
            print('Erro: Opção inválida! Escolha uma opção entre 1 e 4.')

    except ValueError:
        print('Opção invalida digite um numero.')
    
    return True

def main():
    os.system('cls')
    mostrar_menu()
    return escolher_opcao()

while True:
    continuar = main()
    
    if continuar == False:
        break