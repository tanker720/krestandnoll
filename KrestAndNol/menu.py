import random
import os
import tkinter

from bot import Bot
from game import Game
from session import Session

class GUI:
    
    def printText(self, text):
        print(text)

    def clear(self):
        os.system("clear")


class Menu:

    work = True

    def exit(self, gui):
        gui.printText("Спасибо за игру! Приходите еще)")
        self.work = False

    def author(self):
        print("Автор: Волков Юрий")
        print("Группа: 1291-23")

    def quantitywin(self, session):
        print("Количество выйгрышей - {}".format(session.win))

    def quantitymotion(self, session):
        print("Количество попыток - {}".format(session.hod))


    def help(self):
        print("Команды:")
        print("     1) author - показывает автора игры")
        print("     2) quantitymotion или qm - показывать количество попыток")
        print("     3) quantitywin или qw - показывать количество выйгрышей")
        print("     4) go - начинает игру")
        print("     5) exit - выходит игру")

    def start(self):

        session = Session()
        gui = GUI()

        gui.clear()

        gui.printText("XXXКрестики и НоликиOOO create by Yuri Volkov")
        gui.printText("Напишите help что бы узнать команды игры")

        while self.work:
            inputUser = str(input())
            if inputUser == "go":
                g = Game()
                game = g.main(g)
                if game == "win":
                    session.win = session.win + 1
                session.hod = session.hod + 1
                del g
            elif inputUser == "help":
                self.help()
            elif (inputUser == "quantitymotion") | (inputUser == "qm"):
                self.quantitymotion(session)
            elif (inputUser == "quantitywin") | (inputUser == "qw"):
                self.quantitywin(session)
            elif inputUser == "author":
                self.author() 
            elif inputUser == "exit":   
                self.exit(gui)
            else:
                print("Нет такой команды")

if __name__ == "__main__":
    m = Menu()
    m.start()