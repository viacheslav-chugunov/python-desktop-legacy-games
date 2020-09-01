import pygame
from random import randint


class Falling:
    def __init__(self, y, max_x, max_y, speed):
        self.x = randint(0, max_x - 69)
        self.__based_y = y
        self.y = self.__based_y
        self.__max_x = max_x
        self.__max_y = max_y
        self.speed_y = speed
        self.image = pygame.image.load("images/falling.png")

    def update(self):
        if self.y - 69 < self.__max_y:
            self.y += self.speed_y

    def restart(self, speedup=0):
        self.x = randint(0, self.__max_x - 80)
        self.y = self.__based_y
        self.speed_y += speedup
