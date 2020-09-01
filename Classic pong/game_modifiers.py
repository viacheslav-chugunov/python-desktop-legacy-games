# in dev
import arcade


class GameModifiers:

    def __init__(self, scale):
        self.scale = scale

        # speed up
        self.speed_up_sprite = arcade.Sprite('image/mod1.png', self.scale)

        # speed down
        self.speed_down_sprite = arcade.Sprite('image/mod1.png', self.scale)
