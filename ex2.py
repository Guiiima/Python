n = int(input("Informe o tamanho do campo: "))
board = [[0 for i in range(n)] for j in range(n)]

def menu(): 
    """Controla a principal execução do jogo, permitindo jogar novamente ou sair"""
    continuar=1
    while continuar:
        continuar = int(input("1. Jogar novamente\n" + "2. Sair \n"))
        if continuar == 1:
            game()
        elif continuar == 2:
            print("Saindo...")
        else:
            print("Opção inválida!")

def game():
    """Contém a lógica principal do jogo, com o loop de jogadas e verificações."""
    jogada=0

    while ganhou() == 0 and jogada < n*n:  
        print("\nJogador ", jogada%2 + 1)
        exibe()
        linha  = int(input("\nLinha :"))
        coluna = int(input("Coluna:"))

        if 0 < linha <= n and 0 < coluna <= n and board[linha-1][coluna-1] == 0:
            if (jogada%2+1) == 1:
                board[linha-1][coluna-1] = 1
            else:
                board[linha-1][coluna-1] = -1
        else:
            print("Posição inválida ou já ocupada!")
            jogada -= 1

        if ganhou():
            print("Jogador ", jogada%2 + 1, " ganhou após ", jogada + 1, " rodadas")
        jogada += 1

    if jogada == n*n and ganhou() == 0:
        print("Empate!")
        exibe()

def ganhou():
    """Verifica se algum jogador venceu."""
    for i in range(n):
        if sum(board[i]) == n or sum(board[i]) == -n:  
            return 1
        if sum([board[j][i] for j in range(n)]) == n or sum([board[j][i] for j in range(n)]) == -n:  
            return 1

        # Checando diagonais
    if sum([board[i][i] for i in range(n)]) == n or sum([board[i][i] for i in range(n)]) == -n:
        return 1
    if sum([board[i][n-1-i] for i in range(n)]) == n or sum([board[i][n-1-i] for i in range(n)]) == -n:
        return 1

    return 0

def exibe():
    """Mostra o tabuleiro atual."""
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                print(" _ ", end=' ')
            elif board[i][j] == 1:
                print(" X ", end=' ')
            elif board[i][j] == -1:
                print(" O ", end=' ')
        print()

menu()
