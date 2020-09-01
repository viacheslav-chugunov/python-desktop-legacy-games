import tkinter as tk
from random import randint
import sys


class Game:
    def __init__(self):
        self.WIDTH = 600
        self.HEIGHT = 600
        self.game_root = tk.Tk()
        self.game_root.title("Tic-tac-toe")
        self.game_root.geometry(str(self.WIDTH) + "x" + str(self.HEIGHT) + "+50+50")
        self.game_root.resizable(False, False)
        self.button_list = []
        self.__setup_buttons()
        self.__playerX = True
        self.__filled = 0

    def run(self):
        self.game_root.mainloop()

    def __setup_buttons(self):

        def button_clicked(index):
            def func():
                if self.__filled == 9:
                    sys.exit()
                elif self.button_list[index]["text"] == "" and self.__playerX and self.__filled != 9:
                    self.button_list[index]["text"] = "X"
                    self.__playerX = False
                    self.__filled += 1
                    self.__checker()
                    self.__ai()
                    self.__checker()
            return func

        for index in range(9):
            self.button_list.append(tk.Button(self.game_root, text=str(""), width=10, height=5,
                                              command=button_clicked(index), font='Times 27',
                                              bg="#FFFFFF"))

        i = 0
        for dy in (0, self.HEIGHT / 3, self.HEIGHT / 1.5):
            for dx in (0, self.WIDTH / 3, self.WIDTH / 1.5):
                self.button_list[i].place(x=dx, y=dy)
                i += 1

    def __ai(self):
        if self.__filled != 9:
            choice = randint(0, 8)
            if self.button_list[choice]["text"] == "":
                self.button_list[choice]["text"] = "O"
                self.__filled += 1
                self.__playerX = True
            else:
                return self.__ai()

    def __checker(self):
        def checker(indexes, color='#3b4'):
            if self.button_list[indexes[0]]["text"] == self.button_list[indexes[1]]["text"] == \
                    self.button_list[indexes[2]]["text"] and self.button_list[indexes[2]]["text"] != "":
                self.button_list[indexes[0]]["bg"] = color
                self.button_list[indexes[1]]["bg"] = color
                self.button_list[indexes[2]]["bg"] = color
                return True
            return False

        tests = [
            checker((0, 1, 2)),
            checker((3, 4, 5)),
            checker((6, 7, 8)),
            checker((0, 3, 6)),
            checker((1, 4, 7)),
            checker((2, 5, 8)),
            checker((0, 4, 8)),
            checker((2, 4, 6)),
        ]

        for test in tests:
            if test:
                self.__filled = 9
                break
