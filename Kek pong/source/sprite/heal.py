import arcade
from ..config import RESOLUTION, HEAL
from random import randrange


class Heal(arcade.Sprite):
    def __init__(self, min_x, max_x):
        x = randrange(int(min_x), int(max_x))
        y = RESOLUTION[1] * 1.1
        super().__init__('media/images/sprite/heal.png', 2, center_x=x, center_y=y)
        self.speed = HEAL['speed']
        self.change_y = -self.speed
