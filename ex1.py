'''
    1) Crie uma versão do jogo da velha 4x4. As regras são as mesmas da versão 3x3.
        Explicação da estratégia: Baseado nas aulas anteriores eu usei como base nossa experiencia em percorrer listas e jeitos diferentes de fazer os fors
        
        Detalhamento das estruturas usadasDetalhamento das estruturas usadas: foram usados listas para calcular a soma de lihas e colunas, loops para percorrer 
        as linhas e colunas e condicionais para verificação de determinado resultado, matriz para usar uma lista de lista e tambem deixar no formato para jogar o jogo
'''
board = [[0 for i in range(4)] for j in range(4)]

def menu(): 
    continuar=1
    while continuar:
        continuar = int(input("2. Sair \n" + "1. Jogar novamente\n"))
        if continuar:
            game()
        else:
            print("Saindo...")

            """Controla a principal execução do jogo, permitindo jogar novamente ou sair"""


def game():
    jogada=0

    while ganhou() == 0 and jogada < 16:  
        print("\nJogador ", jogada%2 + 1)
        exibe()
        linha  = int(input("\nLinha :"))
        coluna = int(input("Coluna:"))

        if 0 < linha <= 4 and 0 < coluna <= 4 and board[linha-1][coluna-1] == 0:
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

    if jogada == 16 and ganhou() == 0:
        print("Empate!")
        exibe()

        """Contém a lógica principal do jogo, com o loop de jogadas e verificações."""

def ganhou():
    for i in range(4):
        if sum(board[i]) == 4 or sum(board[i]) == -4:  
            return 1
        if sum([board[j][i] for j in range(4)]) == 4 or sum([board[j][i] for j in range(4)]) == -4:  
            return 1

    # Checando diagonais
    if sum([board[i][i] for i in range(4)]) == 4 or sum([board[i][i] for i in range(4)]) == -4:
        return 1
    if sum([board[i][3-i] for i in range(4)]) == 4 or sum([board[i][3-i] for i in range(4)]) == -4:
        return 1

    return 0

    """Verifica se algum jogador venceu."""

def exibe():
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                print(" _ ", end=' ')
            elif board[i][j] == 1:
                print(" X ", end=' ')
            elif board[i][j] == -1:
                print(" O ", end=' ')
        print()
    """Mostra o tabuleiro atual."""
menu()
