import arcade
from ..config import RESOLUTION, BALL
from random import randrange
from time import time


class Ball(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__('media/images/sprite/ball.png', center_x=x, center_y=y)
        self.speed = BALL['speed']

        self._min_x, self._min_y = 0, 0
        self._max_x, self._max_y = RESOLUTION

        self._charge_x = 'left'
        self._charge_y = 'top'

        self.change_x = self.speed
        self.change_y = 0

        self._restart_delay_timer = None
        self._restarting_delay_s = 3

        self.active = True

    def update(self):
        if self.active:
            if self._charge_x == 'left':
                if self.center_x >= self._max_x:
                    self.change_x = -self.speed
                    self._charge_x = 'right'

            elif self._charge_x == 'right':
                if self.center_x <= self._min_x:
                    self.change_x = self.speed
                    self._charge_x = 'left'

            if self._charge_y == 'top':
                if self.center_y >= self._max_y:
                    self.change_y = randrange(-int(self.speed), -int(self.speed / 2))
                    self._charge_y = 'bottom'

            elif self._charge_y == 'bottom':
                if self.center_y <= self._min_y:
                    self.change_y = randrange(int(self.speed / 2), int(self.speed))
                    self._charge_y = 'top'

            super().update()
        else:
            self._restarting_timer()

    def draw(self):
        super().draw()

    def beat_off(self):
        if self._charge_x == 'left':
            self._charge_x = 'right'
        else:
            self._charge_x = 'left'

        self.change_x = -self.change_x
        change_y = randrange(-int(self.speed), int(self.speed))

        if change_y > 0:
            self._charge_y = 'top'
        else:
            self._charge_y = 'bottom'

        self.change_y = change_y

    def restart(self, x, y):
        if self._restarting_delay_s is not None:
            self._restart_delay_timer = time()
            self.active = False
            self.beat_off()
            self.center_x = x
            self.center_y = y

    def _restarting_timer(self):
        if time() - self._restart_delay_timer >= self._restarting_delay_s:
            self._restart_delay_timer = None
            self.active = True
