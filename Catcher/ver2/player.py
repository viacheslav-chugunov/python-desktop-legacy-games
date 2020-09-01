import pygame


class Player:
    def __init__(self, x, y, max_x, max_y):
        self.x = x
        self.y = y
        self.__max_x = max_x
        self.__max_y = max_y
        self.speed_x = 0
        self.image = pygame.image.load("images/beater.png")

    def update(self):
        if self.x <= 0:
            self.x = 0
        elif self.x >= self.__max_x - 186:
            self.x = self.__max_x - 186
        self.x += self.speed_x
