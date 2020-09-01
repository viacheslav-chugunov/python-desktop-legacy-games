import arcade
from source.config import BEATER, RESOLUTION
from time import time


class Beater(arcade.Sprite):
    def __init__(self, x, y, revival_time_s=10, keyboard=False, keys=(None, None)):
        super().__init__('media/images/sprite/beater.png', center_x=x, center_y=y)
        self.speed = BEATER['speed']
        self.hp = BEATER['hp']

        self._move_to = self.center_y
        self.move_to_change = 0
        self._stop_button_pressed = False
        self._activate_timer = None
        self._revival_time_s = revival_time_s
        self._start_y_after_revival = RESOLUTION[1] * .5

        self.active = True
        self._keyboard = keyboard
        self._up_key = keys[0]
        self._down_key = keys[1]

    def move_to_y(self, y):
        self._move_to = y

    def update(self):
        if self.active:
            if not self._keyboard:
                if not self._stop_button_pressed:
                    if self.center_y < self._move_to:
                        self.change_y = self.speed
                    elif self.center_y > self._move_to:
                        self.change_y = -self.speed
                    else:
                        self.change_y = 0
                else:
                    self.change_y = 0
            super().update()
        else:
            self._revival()

        if self.center_y - self.width <= 0:
            self.center_y = self.width
        if self.center_y + self.width >= RESOLUTION[1]:
            self.center_y = RESOLUTION[1] - self.width

    def draw(self):
        if self.active:
            super().draw()

    def stop_moving_on_press(self):
        self._stop_button_pressed = True

    def continue_moving_on_release(self):
        self._stop_button_pressed = False

    def get_hit_on_collision(self):
        self.hp -= 1

    def start_timer_to_activate(self):
        self._activate_timer = time()

    def on_key_press(self, key, mod):
        if key == self._up_key:
            self.change_y = self.speed
        elif key == self._down_key:
            self.change_y = -self.speed

    def on_key_release(self, key, mod):
        if key == self._up_key:
            self.change_y = 0
        elif key == self._down_key:
            self.change_y = 0

    def _revival(self):
        if self._activate_timer is not None:
            if time() - self._activate_timer >= self._revival_time_s:
                self.active = True
                self._activate_timer = None
                self.hp += BEATER['hp']
                self.center_y = self._start_y_after_revival
