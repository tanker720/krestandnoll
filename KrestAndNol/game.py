from bot import Bot
from player import Player
from board import Board

class Game:

    turnToGo = None
    win = None

    def winnerPrint(self):
        print("")
        print("")
        if self.win != "nobody":
            print("Выйграл игрок {}".format(self.win.symbol))
        else:
            print("Ничья")
        
    def winner(self, board, player):
        for w in board.winCom:
            if (board.kletka[w[0] - 1] == player.symbol) & (board.kletka[w[1] - 1] == player.symbol) & (board.kletka[w[2] - 1] == player.symbol):
                self.win = player
                return
        a = []
        for h in board.kletka:
            if h == None:
                a.append(h)
        if a == []:
            self.win = "nobody"

    def printBoard(self, board):
        a = 0
        for k in board.kletka:
            if (a % 3 == 0):
                print("")
            print("{}".format(k), end=" ")
            a += 1
        print("")

    
    def choicePlayer(self):

        print("Выберите символ которым вы хотите ходить. X или O?")

        while True:
            choice = str(input())
            if (choice == "X") | (choice == "x") | (choice =="х") | (choice == "Х"):
                return "X"
            elif (choice == "O") | (choice == "o") | (choice == "0") | (choice == "о") | (choice == "О"):
                return "O"
            else:
                print("Неправильный символ. Выберите X илм O")


    def main(self, game):

        b = Board()

        choicePlayer = self.choicePlayer()

        p = Player(choicePlayer)

        if choicePlayer == "X":
            bot = Bot("O")
        else:
            bot = Bot("X")

        self.turnToGo = p

        while self.win == None:
            if self.win == None:
                if self.turnToGo == p:
                    p.hodPlayer(b, p, game)
                    self.turnToGo = Bot
                else:
                    print("Ходит игрок Bot")
                    bot.hod(b)
                    self.winner(b, bot)
                    self.turnToGo = p
                #   os.system("clear")
                self.printBoard(b)
        self.winnerPrint()
        if self.win == p:
            return  "win"
        else:
            return "loss"
        del b