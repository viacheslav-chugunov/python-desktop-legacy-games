import arcade


class Beater:
    def __init__(self, x_pos, y_pos, x_max, y_max, scale=1, width=200, height=45, speed=20):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.__scale = scale
        self.__x_max = x_max
        self.__y_max = y_max
        self.width = width
        self.height = height
        self.speed = speed
        self.x_change = 0

        self.sprite = arcade.Sprite("images/beater.png", 1)
        self.sprite.set_position(self.x_pos, self.y_pos)
        self.sprite.width = self.width
        self.sprite.height = self.height

    def draw(self):
        self.sprite.draw()

    def update(self):
        if self.width / 4 < self.x_pos + self.x_change < self.__x_max - self.width / 4:
            self.x_pos += self.x_change
            self.sprite.set_position(self.x_pos, self.y_pos)


