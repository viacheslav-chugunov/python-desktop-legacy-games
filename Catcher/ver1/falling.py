import arcade
import random


class Falling:
    def __init__(self, x_max, y_max, scale=1, width=60, height=35, speed=3):
        self.x_pos = random.randint(10, x_max - 10)
        self.y_pos = y_max + 15
        self.__x_max = x_max
        self.__y_max = y_max
        self.__scale = scale
        self.__width = width
        self.__height = height
        self.speed = speed

        self.sprite = arcade.Sprite("images/falling.png", self.__scale)
        self.sprite.set_position(self.x_pos, self.y_pos)
        self.sprite.width = self.__width
        self.sprite.height = self.__height

    def draw(self):
        self.sprite.draw()

    def update(self):
        if self.y_pos > -self.__height:
            self.y_pos -= self.speed
            self.sprite.set_position(self.x_pos, self.y_pos)

    def restart(self):
        self.x_pos = random.randint(10, self.__x_max - 10)
        self.y_pos = self.__y_max




