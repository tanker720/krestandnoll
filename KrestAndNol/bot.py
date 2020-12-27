import random

class Bot:

    symbol  = None

    def __init__(self, symbol):
        self.symbol = symbol

    def hod(self, board):

        while True:
            num = int(random.uniform(0, 8))
            if board.kletka[num] == None:
                board.kletka[num] = self.symbol
                return