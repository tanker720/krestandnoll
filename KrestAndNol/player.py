

class Player:

    symbol = None

    def __init__(self, symbol):
        self.symbol = symbol

    def hodPlayer(self, board, player, game):

        print("Ваша очередь ходить")

        while True:
            hod = int(input()) - 1
            if (hod <= 8) & (hod >= 0):
                if board.kletka[hod] == None:
                    board.kletka[hod] = player.symbol
                    game.winner(board, player)
                    return 
                else:
                    print("Клетка занята, выберите другую")
            else:
                print("Такой клетки нет")