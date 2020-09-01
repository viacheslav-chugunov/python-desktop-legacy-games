import arcade


class Player:

    def __init__(self, x, y, scale, speed, texture):
        self.x = x
        self.y = y
        self.scale = scale
        self.speed = speed
        self.change_x = 0
        self.change_y = 0
        self.texture = texture
        self.sprite = arcade.Sprite(texture, self.scale,
                                    center_x=self.x, center_y=self.y)

