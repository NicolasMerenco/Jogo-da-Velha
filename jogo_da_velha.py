import random

def exibir_tabuleiro(tab):
    print("\n")
    print(" " + tab[0] + " | " + tab[1] + " | " + tab[2])
    print("---|---|---")
    print(" " + tab[3] + " | " + tab[4] + " | " + tab[5])
    print("---|---|---")
    print(" " + tab[6] + " | " + tab[7] + " | " + tab[8])
    print("\n")

def checar_vitoria(tab, jogador):
    combinacoes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # colunas
        [0, 4, 8], [2, 4, 6]              # diagonais
    ]
    for linha in combinacoes:
        if tab[linha[0]] == tab[linha[1]] == tab[linha[2]] == jogador:
            return True
    return False

def checar_empate(tab):
    return ' ' not in tab

def jogada_valida(tab, pos):
    return tab[pos] == ' '

def jogada_jogador(tab, jogador):
    while True:
        try:
            pos = int(input(f"Jogador {jogador}, escolha uma posição (1-9): ")) - 1
            if 0 <= pos <= 8 and jogada_valida(tab, pos):
                tab[pos] = jogador
                break
            else:
                print("Jogada inválida. Tente novamente.")
        except ValueError:
            print("Digite um número válido.")

def jogada_computador(tab):
    print("Computador pensando...")
    # Estratégia simples: vencer, bloquear ou jogar aleatório
    for i in range(9):
        if tab[i] == ' ':
            tab_copia = tab[:]
            tab_copia[i] = 'O'
            if checar_vitoria(tab_copia, 'O'):
                tab[i] = 'O'
                return

    for i in range(9):
        if tab[i] == ' ':
            tab_copia = tab[:]
            tab_copia[i] = 'X'
            if checar_vitoria(tab_copia, 'X'):
                tab[i] = 'O'
                return

    escolhas = [i for i in range(9) if tab[i] == ' ']
    if escolhas:
        tab[random.choice(escolhas)] = 'O'

def menu():
    print("=== JOGO DA VELHA ===")
    print("1. Jogador vs Jogador")
    print("2. Jogador vs Computador")
    print("0. Sair")
    return input("Escolha uma opção: ")

def jogo_vs_jogador():
    tab = [' '] * 9
    jogador_atual = 'X'
    while True:
        exibir_tabuleiro(tab)
        jogada_jogador(tab, jogador_atual)
        if checar_vitoria(tab, jogador_atual):
            exibir_tabuleiro(tab)
            print(f"Jogador {jogador_atual} venceu!")
            break
        elif checar_empate(tab):
            exibir_tabuleiro(tab)
            print("Empate!")
            break
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'

def jogo_vs_computador():
    tab = [' '] * 9
    jogador_atual = 'X'
    while True:
        exibir_tabuleiro(tab)
        if jogador_atual == 'X':
            jogada_jogador(tab, 'X')
        else:
            jogada_computador(tab)
        if checar_vitoria(tab, jogador_atual):
            exibir_tabuleiro(tab)
            if jogador_atual == 'X':
                print("Você venceu!")
            else:
                print("O computador venceu!")
            break
        elif checar_empate(tab):
            exibir_tabuleiro(tab)
            print("Empate!")
            break
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'

def main():
    while True:
        opcao = menu()
        if opcao == '1':
            jogo_vs_jogador()
        elif opcao == '2':
            jogo_vs_computador()
        elif opcao == '0':
            print("Saindo do jogo. Até a próxima!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
