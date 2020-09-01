import arcade


class Ball:

    def __init__(self, x, y, scale, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.change_x = self.speed
        self.change_y = self.speed
        self.scale = scale
        self.sprite = arcade.Sprite('image/ball.png', self.scale,
                                    center_x=self.x, center_y=self.y)

